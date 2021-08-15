# Generated by Django 3.2.3 on 2021-08-15 12:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('teams', '0001_initial'),
        ('fees', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlayerFees',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='player_fees_fee', to='fees.fee')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='player_fees_player', to=settings.AUTH_USER_MODEL)),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='player_fees_team', to='teams.team')),
            ],
        ),
    ]
