# Generated by Django 2.2.1 on 2019-11-20 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0007_auto_20191120_1549'),
    ]

    operations = [
        migrations.AddField(
            model_name='tiremanagementhistory',
            name='tire_mileage',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='tiremanagementhistory',
            name='vehicle_mileage',
            field=models.FloatField(default=0),
        ),
    ]
