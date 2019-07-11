# Generated by Django 2.2.1 on 2019-07-11 14:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('vehicle', '0001_initial'),
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ParkingRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_time', models.DateTimeField(auto_now_add=True)),
                ('approved', models.BooleanField(default=False)),
                ('approved_time', models.DateTimeField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('place', models.CharField(max_length=100)),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='parking_requests_as_driver', to=settings.AUTH_USER_MODEL)),
                ('escort', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='parking_requests_as_escort', to=settings.AUTH_USER_MODEL)),
                ('job', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='order.Job')),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='parking_requests', to='vehicle.Vehicle')),
            ],
            options={
                'ordering': ['approved', '-approved_time', '-request_time'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RestRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_time', models.DateTimeField(auto_now_add=True)),
                ('approved', models.BooleanField(default=False)),
                ('approved_time', models.DateTimeField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('category', models.PositiveIntegerField(choices=[(0, '病假'), (1, '私事')], default=0)),
                ('from_date', models.DateField()),
                ('to_date', models.DateField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['approved', '-approved_time', '-request_time'],
                'unique_together': {('user', 'from_date', 'to_date')},
            },
        ),
        migrations.CreateModel(
            name='EscortChangeRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_time', models.DateTimeField(auto_now_add=True)),
                ('approved', models.BooleanField(default=False)),
                ('approved_time', models.DateTimeField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('change_time', models.DateTimeField(blank=True, null=True)),
                ('change_place', models.CharField(blank=True, max_length=100, null=True)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.Job')),
                ('new_escort', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='escort_change_assigned', to=settings.AUTH_USER_MODEL)),
                ('old_escort', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='escort_change_requests', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['approved', '-approved_time', '-request_time'],
                'unique_together': {('job', 'old_escort')},
            },
        ),
        migrations.CreateModel(
            name='DriverChangeRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_time', models.DateTimeField(auto_now_add=True)),
                ('approved', models.BooleanField(default=False)),
                ('approved_time', models.DateTimeField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('change_time', models.DateTimeField(blank=True, null=True)),
                ('change_place', models.CharField(blank=True, max_length=100, null=True)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.Job')),
                ('new_driver', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='driver_change_assigned', to=settings.AUTH_USER_MODEL)),
                ('old_driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='driver_change_requests', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['approved', '-approved_time', '-request_time'],
                'unique_together': {('job', 'old_driver')},
            },
        ),
    ]
