# Generated by Django 2.2.1 on 2019-10-08 14:04

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('security', '0002_companypolicyread'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='companypolicyread',
            unique_together={('policy', 'user')},
        ),
    ]