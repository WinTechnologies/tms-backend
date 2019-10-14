# Generated by Django 2.2.1 on 2019-10-14 21:53

from django.conf import settings
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('info', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FuelConsumption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('vehicle_type', models.CharField(max_length=100)),
                ('high_way', models.FloatField(default=0)),
                ('normal_way', models.FloatField(default=0)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'ordering': ('-updated',),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TireManagementHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('installed_on', models.DateTimeField()),
                ('mileage', models.FloatField(blank=True, null=True)),
                ('mileage_limit', models.FloatField(default=0)),
                ('brand', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
                ('tire_type', models.CharField(max_length=100)),
                ('tread_depth', models.FloatField(default=0)),
                ('manufacturer', models.CharField(max_length=100)),
                ('contact_number', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ['-installed_on'],
            },
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('model', models.CharField(choices=[('T', '牵引车'), ('S', '半挂罐车')], default='T', max_length=1)),
                ('plate_num', models.CharField(max_length=100, unique=True)),
                ('identifier_code', models.CharField(max_length=100)),
                ('brand', models.CharField(choices=[('T', '通华'), ('L', '解放'), ('Y', '扬州中集')], default='T', max_length=1)),
                ('use_for', models.CharField(blank=True, max_length=100, null=True)),
                ('total_load', models.FloatField(default=0)),
                ('actual_load', models.FloatField(default=0)),
                ('model_2', models.CharField(choices=[('T', '牵引车'), ('S', '半挂罐车')], default='T', max_length=1)),
                ('plate_num_2', models.CharField(max_length=100, unique=True)),
                ('identifier_code_2', models.CharField(max_length=100)),
                ('brand_2', models.CharField(choices=[('T', '通华'), ('L', '解放'), ('Y', '扬州中集')], default='T', max_length=1)),
                ('use_for_2', models.CharField(blank=True, max_length=100, null=True)),
                ('total_load_2', models.FloatField(default=0)),
                ('actual_load_2', models.FloatField(default=0)),
                ('affiliation_unit', models.CharField(blank=True, max_length=100, null=True)),
                ('use_started_on', models.DateField(blank=True, null=True)),
                ('use_expires_on', models.DateField(blank=True, null=True)),
                ('service_area', models.CharField(blank=True, max_length=100, null=True)),
                ('obtain_method', models.CharField(blank=True, max_length=100, null=True)),
                ('attribute', models.CharField(blank=True, max_length=100, null=True)),
                ('cert_type', models.CharField(blank=True, max_length=100, null=True)),
                ('cert_id', models.CharField(blank=True, max_length=100, null=True)),
                ('cert_authority', models.CharField(blank=True, max_length=100, null=True)),
                ('cert_registered_on', models.DateField(blank=True, null=True)),
                ('cert_active_on', models.DateField(blank=True, null=True)),
                ('cert_expires_on', models.DateField(blank=True, null=True)),
                ('insurance_active_on', models.DateField(blank=True, null=True)),
                ('insurance_expires_on', models.DateField(blank=True, null=True)),
                ('cert_type_2', models.CharField(blank=True, max_length=100, null=True)),
                ('cert_id_2', models.CharField(blank=True, max_length=100, null=True)),
                ('cert_authority_2', models.CharField(blank=True, max_length=100, null=True)),
                ('cert_registered_on_2', models.DateField(blank=True, null=True)),
                ('cert_active_on_2', models.DateField(blank=True, null=True)),
                ('cert_expires_on_2', models.DateField(blank=True, null=True)),
                ('insurance_active_on_2', models.DateField(blank=True, null=True)),
                ('insurance_expires_on_2', models.DateField(blank=True, null=True)),
                ('branches', django.contrib.postgres.fields.ArrayField(base_field=models.PositiveIntegerField(), size=None)),
                ('engine_model', models.CharField(blank=True, max_length=100, null=True)),
                ('engine_power', models.PositiveIntegerField(blank=True, null=True)),
                ('transmission_model', models.CharField(blank=True, max_length=100, null=True)),
                ('engine_displacement', models.CharField(blank=True, max_length=100, null=True)),
                ('tire_rules', models.CharField(blank=True, max_length=100, null=True)),
                ('tank_material', models.CharField(blank=True, max_length=100, null=True)),
                ('is_gps_installed', models.BooleanField(default=False)),
                ('is_gps_working', models.BooleanField(default=False)),
                ('with_pump', models.BooleanField(default=False)),
                ('main_car_size', models.CharField(blank=True, max_length=100, null=True)),
                ('main_car_color', models.CharField(blank=True, max_length=100, null=True)),
                ('trailer_car_size', models.CharField(blank=True, max_length=100, null=True)),
                ('trailer_car_color', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('status', models.CharField(choices=[('A', 'Available'), ('P', 'In Work'), ('R', 'Repair')], default='A', max_length=1)),
            ],
            options={
                'ordering': ['-updated'],
            },
        ),
        migrations.CreateModel(
            name='VehicleAfterDrivingItemCheck',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_checked', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='VehicleBeforeDrivingItemCheck',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_checked', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='VehicleCheckHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('before_driving_problems', models.PositiveIntegerField(default=0)),
                ('before_driving_description', models.TextField(blank=True, null=True)),
                ('before_driving_checked_time', models.DateTimeField(blank=True, null=True)),
                ('driving_problems', models.PositiveIntegerField(default=0)),
                ('driving_description', models.TextField(blank=True, null=True)),
                ('driving_checked_time', models.DateTimeField(blank=True, null=True)),
                ('after_driving_problems', models.PositiveIntegerField(default=0)),
                ('after_driving_description', models.TextField(blank=True, null=True)),
                ('after_driving_checked_time', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'ordering': ['driver', '-before_driving_checked_time'],
            },
        ),
        migrations.CreateModel(
            name='VehicleCheckItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('is_before_driving_item', models.BooleanField(default=False)),
                ('is_driving_item', models.BooleanField(default=False)),
                ('is_after_driving_item', models.BooleanField(default=False)),
                ('is_published', models.BooleanField(default=False)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'ordering': ('-updated',),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='VehicleTire',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('position', models.PositiveIntegerField(default=0)),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vehicle.Vehicle')),
            ],
            options={
                'unique_together': {('vehicle', 'position')},
            },
        ),
        migrations.CreateModel(
            name='VehicleMaintenanceHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('category', models.PositiveIntegerField(choices=[(0, '驱动轮'), (1, '齿轮油')], default=0)),
                ('maintenance_date', models.DateField()),
                ('total_cost', models.FloatField(default=0)),
                ('mileage', models.FloatField(default=0)),
                ('accessories_fee', models.FloatField(default=0)),
                ('work_fee', models.FloatField(default=0)),
                ('ticket_type', models.CharField(blank=True, max_length=100, null=True)),
                ('tax_rate', models.FloatField(default=0)),
                ('description', models.TextField(blank=True, null=True)),
                ('assignee', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('station', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='info.Station')),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vehicle.Vehicle')),
            ],
            options={
                'ordering': ('-updated',),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='VehicleDrivingItemCheck',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_checked', models.BooleanField(default=False)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vehicle.VehicleCheckItem')),
                ('vehicle_check_history', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vehicle.VehicleCheckHistory')),
            ],
        ),
        migrations.CreateModel(
            name='VehicleDriverEscortBind',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('driver', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='vehicles_as_driver', to=settings.AUTH_USER_MODEL)),
                ('escort', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='vehicles_as_escort', to=settings.AUTH_USER_MODEL)),
                ('vehicle', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='bind', to='vehicle.Vehicle')),
            ],
        ),
        migrations.CreateModel(
            name='VehicleDriverDailyBind',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('get_on', models.DateTimeField(auto_now_add=True)),
                ('get_off', models.DateTimeField(blank=True, null=True)),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='my_vehicle_bind', to=settings.AUTH_USER_MODEL)),
                ('get_off_station', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='info.Station')),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vehicle.Vehicle')),
            ],
            options={
                'ordering': ['-get_on', 'vehicle'],
            },
        ),
        migrations.AddField(
            model_name='vehiclecheckhistory',
            name='after_driving_checked_items',
            field=models.ManyToManyField(related_name='afters', through='vehicle.VehicleAfterDrivingItemCheck', to='vehicle.VehicleCheckItem'),
        ),
        migrations.AddField(
            model_name='vehiclecheckhistory',
            name='before_driving_checked_items',
            field=models.ManyToManyField(related_name='befores', through='vehicle.VehicleBeforeDrivingItemCheck', to='vehicle.VehicleCheckItem'),
        ),
        migrations.AddField(
            model_name='vehiclecheckhistory',
            name='driver',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='my_vehicle_checks', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='vehiclecheckhistory',
            name='driving_checked_items',
            field=models.ManyToManyField(related_name='drivings', through='vehicle.VehicleDrivingItemCheck', to='vehicle.VehicleCheckItem'),
        ),
        migrations.AddField(
            model_name='vehiclecheckhistory',
            name='vehicle',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vehicle.Vehicle'),
        ),
        migrations.CreateModel(
            name='VehicleCheckDocument',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document_type', models.CharField(choices=[('B', '行车前'), ('D', '行车中'), ('A', '行车后')], default='B', max_length=1)),
                ('document', models.ImageField(upload_to='')),
                ('vehicle_check_history', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='vehicle.VehicleCheckHistory')),
            ],
        ),
        migrations.AddField(
            model_name='vehiclebeforedrivingitemcheck',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vehicle.VehicleCheckItem'),
        ),
        migrations.AddField(
            model_name='vehiclebeforedrivingitemcheck',
            name='vehicle_check_history',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vehicle.VehicleCheckHistory'),
        ),
        migrations.AddField(
            model_name='vehicleafterdrivingitemcheck',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vehicle.VehicleCheckItem'),
        ),
        migrations.AddField(
            model_name='vehicleafterdrivingitemcheck',
            name='vehicle_check_history',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vehicle.VehicleCheckHistory'),
        ),
        migrations.CreateModel(
            name='TireTreadDepthCheckHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('tread_depth', models.FloatField(default=0)),
                ('checked_on', models.DateTimeField(auto_now_add=True)),
                ('tire', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='history', to='vehicle.TireManagementHistory')),
            ],
            options={
                'ordering': ('-checked_on',),
            },
        ),
        migrations.AddField(
            model_name='tiremanagementhistory',
            name='vehicle_tire',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='history', to='vehicle.VehicleTire'),
        ),
    ]
