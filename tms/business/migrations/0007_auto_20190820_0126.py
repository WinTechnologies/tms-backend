# Generated by Django 2.2.1 on 2019-08-19 17:26

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0006_auto_20190820_0125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restrequest',
            name='ccs',
            field=models.ManyToManyField(related_name='rest_request_as_cc', through='business.RestRequestCC', to=settings.AUTH_USER_MODEL),
        ),
    ]