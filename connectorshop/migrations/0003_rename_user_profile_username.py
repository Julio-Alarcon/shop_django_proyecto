# Generated by Django 4.1.6 on 2023-02-11 05:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('connectorshop', '0002_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='user',
            new_name='username',
        ),
    ]
