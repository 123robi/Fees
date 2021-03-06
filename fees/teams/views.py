from django.db.models import Prefetch
from rest_framework import mixins, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from fees.fees.models import Fee
from fees.fees.serializers import FeeSerializer
from fees.teams.models import Team
from fees.teams.serializers import TeamSerializer, TeamListSerializer, TeamRetrieveSerializer
from fees.users.models import User
from fees.users.serializers import UserSerializer


class TeamViewSet(mixins.CreateModelMixin,
                  mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  viewsets.GenericViewSet):
    serializer_class = TeamSerializer
    queryset = Team.objects.all()
    permission_classes = (IsAuthenticated,)

    def get_serializer_class(self):
        if self.action == 'list':
            return TeamListSerializer
        elif self.action == 'retrieve':
            return TeamRetrieveSerializer
        return super().get_serializer_class()

    def get_queryset(self, *args, **kwargs):
        return Team.objects.filter(players__in=[self.request.user])

    def perform_create(self, serializer):
        if "players" not in serializer.validated_data:
            serializer.validated_data["players"] = [str(self.request.user.id)]
        elif self.request.user.id not in serializer.validated_data["players"]:
            serializer.validated_data["players"].append(str(self.request.user.id))

        if "admins" not in serializer.validated_data:
            serializer.validated_data["admins"] = [str(self.request.user.id)]
        elif self.request.user.id not in serializer.validated_data["admins"]:
            serializer.validated_data["admins"].append(str(self.request.user.id))

        return super().perform_create(serializer)

    def retrieve(self, request, *args, **kwargs):
        instance = Team.objects.filter(**kwargs).prefetch_related("players").prefetch_related(
            "admins").prefetch_related("player_fees_team__fee").prefetch_related("player_fees_team__player").first()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    @action(methods=['get'], detail=True)
    def get_fees_and_players(self, request, pk=None):
        team = Team.objects.get(id=pk)
        players = UserSerializer(team.players.all(), many=True)
        fees = FeeSerializer(Fee.objects.filter(team=team), many=True)
        return Response({
            "players": players.data,
            "fees": fees.data
        })
