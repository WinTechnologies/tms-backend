# Generated by Django 2.2.1 on 2019-08-23 16:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0020_auto_20190824_0032'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='vehiclecheckhistory',
            options={'ordering': ['driver', '-before_driving_checked_time']},
        ),
    ]
