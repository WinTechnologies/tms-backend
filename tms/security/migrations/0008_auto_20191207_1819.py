# Generated by Django 2.2.1 on 2019-12-07 18:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('security', '0007_auto_20191207_1756'),
    ]

    operations = [
        migrations.RenameField(
            model_name='securityissue',
            old_name='check_on',
            new_name='checked_on',
        ),
    ]