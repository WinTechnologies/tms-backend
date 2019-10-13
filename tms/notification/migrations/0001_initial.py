# Generated by Django 2.2.1 on 2019-10-13 22:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import jsonfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('msg_type', models.PositiveIntegerField(choices=[(0, 'New Job Notification'), (1, 'Update Job Notification'), (2, 'Delete Job Notification'), (4, 'Enter Area Notification'), (5, 'Exit Area Notification'), (6, 'Enter Black Dot Notification'), (7, 'Exit Black Dot Notification'), (10, 'Rest Request Notification'), (11, 'Rest Request Notification Approved'), (12, 'Rest Request Notification Declined'), (20, 'Vehicle Maintenance Notification'), (21, 'Vehicle Maintenance Notification Approved'), (22, 'Vehicle Maintenance Notification Declined'), (30, 'Parking Request Notification'), (31, 'Parking Request Notification Approved'), (32, 'Parking Request Notification Declined'), (40, 'Driver Change Notification'), (41, 'Driver Change Notification Approved'), (42, 'Driver Change Notification Declined'), (43, 'Driver Change Notification New Driver'), (50, 'Escort Change Notification'), (51, 'Escort Change Notification Approved'), (52, 'Escort Change Notification Declined'), (53, 'Escort Change Notification New Escort'), (60, 'Traffic Accident Notification')], default=0)),
                ('message', jsonfield.fields.JSONField()),
                ('is_read', models.BooleanField(default=False)),
                ('sent_on', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notifications', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('is_read', '-sent_on'),
            },
        ),
    ]
