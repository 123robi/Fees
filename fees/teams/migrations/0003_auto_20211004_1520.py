# Generated by Django 3.2.3 on 2021-10-04 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='account_number',
            field=models.CharField(blank=True, max_length=128, verbose_name='Account number'),
        ),
        migrations.AddField(
            model_name='team',
            name='bank_code',
            field=models.CharField(blank=True, max_length=128, verbose_name='Bank code'),
        ),
    ]
