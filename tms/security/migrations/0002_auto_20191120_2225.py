# Generated by Django 2.2.1 on 2019-11-20 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hr', '0002_auto_20191120_2133'),
        ('security', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='test',
            name='appliants',
        ),
        migrations.AddField(
            model_name='test',
            name='departments',
            field=models.ManyToManyField(to='hr.Department'),
        ),
    ]