# Generated by Django 2.2.17 on 2021-01-29 12:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Userprofile', '0004_auto_20210126_2315'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='Userimg',
        ),
    ]
