# Generated by Django 3.1.2 on 2022-04-05 10:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('uweflix', '0005_auto_20220405_1142'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='account_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]