# Generated by Django 2.2.1 on 2019-07-23 16:15

from django.conf import settings
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion
import month.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('info', '0001_initial'),
        ('vehicle', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hr', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('progress', models.PositiveIntegerField(default=1)),
                ('start_due_time', models.DateTimeField(blank=True, null=True)),
                ('finish_due_time', models.DateTimeField(blank=True, null=True)),
                ('started_on', models.DateTimeField(blank=True, null=True)),
                ('finished_on', models.DateTimeField(blank=True, null=True)),
                ('total_weight', models.FloatField(default=0)),
                ('total_mileage', models.FloatField(default=0)),
                ('empty_mileage', models.FloatField(default=0)),
                ('heavy_mileage', models.FloatField(default=0)),
                ('highway_mileage', models.FloatField(blank=True, null=True)),
                ('normalway_mileage', models.FloatField(blank=True, null=True)),
                ('is_paid', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='JobBill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('amount', models.FloatField(default=0)),
                ('unit_price', models.FloatField(default=0)),
                ('cost', models.FloatField(default=0)),
                ('document', models.ImageField(blank=True, null=True, upload_to='')),
                ('category', models.PositiveIntegerField(choices=[(0, '加油'), (1, '路票'), (2, '其他')], default=0)),
                ('sub_category', models.PositiveIntegerField(default=0)),
                ('detail_category', models.PositiveIntegerField(default=0)),
            ],
            options={
                'ordering': ['category', 'sub_category', 'detail_category'],
            },
        ),
        migrations.CreateModel(
            name='JobStation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('step', models.PositiveIntegerField()),
                ('arrived_station_on', models.DateTimeField(blank=True, null=True)),
                ('started_working_on', models.DateTimeField(blank=True, null=True)),
                ('finished_working_on', models.DateTimeField(blank=True, null=True)),
                ('departure_station_on', models.DateTimeField(blank=True, null=True)),
                ('is_completed', models.BooleanField(default=False)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.Job')),
            ],
            options={
                'ordering': ['job', 'step'],
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('alias', models.CharField(max_length=100)),
                ('start_due_time', models.DateTimeField(blank=True, null=True)),
                ('finish_due_time', models.DateTimeField(blank=True, null=True)),
                ('order_source', models.CharField(choices=[('I', '内部'), ('C', 'App')], default='I', max_length=1)),
                ('status', models.CharField(choices=[('P', '未开始'), ('I', '已开始'), ('C', '已完成')], default='P', max_length=1)),
                ('is_same_station', models.BooleanField(default=False)),
                ('assignee', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='charge_orders', to=settings.AUTH_USER_MODEL)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='hr.CustomerProfile')),
                ('loading_station', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders_as_loading_station', to='info.Station')),
            ],
            options={
                'ordering': ['-updated'],
            },
        ),
        migrations.CreateModel(
            name='OrderProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_weight', models.FloatField()),
                ('total_weight_measure_unit', models.CharField(choices=[('L', '公升'), ('T', '吨')], default='T', max_length=1)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('price_weight_measure_unit', models.CharField(choices=[('L', '公升'), ('T', '吨')], default='T', max_length=1)),
                ('loss', models.FloatField()),
                ('loss_unit', models.CharField(choices=[('L', '公升'), ('T', '吨')], default='T', max_length=2)),
                ('payment_method', models.CharField(choices=[('T', '吨'), ('D', '吨/公里'), ('P', '一口价')], default='T', max_length=1)),
                ('is_split', models.BooleanField(default=False)),
                ('is_pump', models.BooleanField(default=False)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.Order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='info.Product')),
            ],
        ),
        migrations.CreateModel(
            name='OrderProductDeliver',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('arriving_due_time', models.DateTimeField()),
                ('weight', models.FloatField()),
                ('order_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.OrderProduct')),
                ('unloading_station', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='info.Station')),
            ],
        ),
        migrations.AddField(
            model_name='orderproduct',
            name='unloading_stations',
            field=models.ManyToManyField(through='order.OrderProductDeliver', to='info.Station'),
        ),
        migrations.AddField(
            model_name='order',
            name='products',
            field=models.ManyToManyField(through='order.OrderProduct', to='info.Product'),
        ),
        migrations.AddField(
            model_name='order',
            name='quality_station',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders_as_quality_station', to='info.Station'),
        ),
        migrations.CreateModel(
            name='JobStationProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mission_weight', models.FloatField(default=0)),
                ('weight', models.FloatField(default=0)),
                ('document', models.ImageField(blank=True, null=True, upload_to='')),
                ('branches', django.contrib.postgres.fields.ArrayField(base_field=models.PositiveIntegerField(), default=list, size=None)),
                ('job_station', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.JobStation')),
                ('orderproductdeliver', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='job_delivers', to='order.OrderProductDeliver')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='info.Product')),
            ],
        ),
        migrations.AddField(
            model_name='jobstation',
            name='products',
            field=models.ManyToManyField(through='order.JobStationProduct', to='info.Product'),
        ),
        migrations.AddField(
            model_name='jobstation',
            name='station',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='info.Station'),
        ),
        migrations.CreateModel(
            name='JobReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month', month.models.MonthField()),
                ('total_mileage', models.PositiveIntegerField(blank=True, null=True)),
                ('empty_mileage', models.PositiveIntegerField(blank=True, null=True)),
                ('heavy_mileage', models.PositiveIntegerField(blank=True, null=True)),
                ('highway_mileage', models.PositiveIntegerField(blank=True, null=True)),
                ('normalway_mileage', models.PositiveIntegerField(blank=True, null=True)),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='report', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('month',),
            },
        ),
        migrations.AddField(
            model_name='job',
            name='bills',
            field=models.ManyToManyField(blank=True, to='order.JobBill'),
        ),
        migrations.AddField(
            model_name='job',
            name='driver',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jobs_as_driver', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='job',
            name='escort',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jobs_as_escort', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='job',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jobs', to='order.Order'),
        ),
        migrations.AddField(
            model_name='job',
            name='route',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='info.Route'),
        ),
        migrations.AddField(
            model_name='job',
            name='stations',
            field=models.ManyToManyField(through='order.JobStation', to='info.Station'),
        ),
        migrations.AddField(
            model_name='job',
            name='vehicle',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jobs', to='vehicle.Vehicle'),
        ),
        migrations.CreateModel(
            name='VehicleUserBind',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bind_method', models.CharField(choices=[('A', 'By Admin'), ('J', 'By Job')], default='A', max_length=1)),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vehicles_as_driver', to=settings.AUTH_USER_MODEL)),
                ('escort', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vehicles_as_escort', to=settings.AUTH_USER_MODEL)),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vehicle.Vehicle')),
            ],
            options={
                'unique_together': {('vehicle', 'driver', 'escort')},
            },
        ),
    ]
