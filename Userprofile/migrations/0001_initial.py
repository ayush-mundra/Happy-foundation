# Generated by Django 2.2.17 on 2021-01-26 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(default='SOME STRING', max_length=200)),
                ('Phone', models.CharField(default='SOME STRING', max_length=20)),
                ('address', models.CharField(default='SOME STRING', max_length=200)),
                ('Userimg', models.ImageField(upload_to='User/')),
            ],
        ),
    ]