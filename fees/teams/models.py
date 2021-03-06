from django.db import models

from fees.users.models import User


class Team(models.Model):
    name = models.CharField('Name', max_length=128)
    players = models.ManyToManyField(User, related_name='player_team', blank=True)
    admins = models.ManyToManyField(User, related_name='admin_team', blank=True)

    currency = models.CharField('Currency', max_length=128)

    account_prefix = models.CharField('Account prefix', max_length=128, blank=True)
    account_number = models.CharField('Account number', max_length=128, blank=True)
    bank_code = models.CharField('Bank code', max_length=128, blank=True)

    def __str__(self):
        return self.name

