# Generated by Django 3.2.3 on 2021-08-24 12:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0002_team_admins'),
        ('fees', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fee',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team_fees', to='teams.team'),
        ),
    ]
