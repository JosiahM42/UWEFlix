# Generated by Django 3.1.2 on 2022-03-21 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uweflix', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='is_cinema_accounts',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='account',
            name='is_cinema_admin',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='account',
            name='is_club',
            field=models.BooleanField(default=False),
        ),
    ]
