# Generated by Django 2.2.17 on 2021-03-21 16:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Userprofile', '0008_profile_owner2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='Username',
        ),
        migrations.AlterField(
            model_name='profile',
            name='owner2',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
