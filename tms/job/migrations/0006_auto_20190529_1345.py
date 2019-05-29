# Generated by Django 2.2.1 on 2019-05-29 13:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0005_drivernotification'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='vehicle',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jobs', to='vehicle.Vehicle'),
        ),
    ]
