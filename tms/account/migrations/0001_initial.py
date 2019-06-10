# Generated by Django 2.2.1 on 2019-06-10 14:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import tms.core.validations


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('info', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=100, unique=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True, unique=True)),
                ('mobile', models.CharField(blank=True, max_length=20, null=True, unique=True, validators=[tms.core.validations.validate_mobile])),
                ('device_token', models.CharField(blank=True, max_length=100, null=True, unique=True)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('last_seen', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('role', models.CharField(choices=[('A', '管理人员'), ('S', '工作人员'), ('D', '驾驶人员'), ('E', '押运人员'), ('C', '客户')], default='S', max_length=1)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='StaffProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_card', models.CharField(blank=True, max_length=100, null=True)),
                ('birthday', models.DateField(blank=True, null=True)),
                ('emergency_number', models.CharField(blank=True, max_length=100, null=True)),
                ('spouse_name', models.CharField(blank=True, max_length=100, null=True)),
                ('spouse_number', models.CharField(blank=True, max_length=100, null=True)),
                ('parent_name', models.CharField(blank=True, max_length=100, null=True)),
                ('parent_number', models.CharField(blank=True, max_length=100, null=True)),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='staff_profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='StaffDocument',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('no', models.CharField(max_length=100)),
                ('document_type', models.CharField(choices=[('1', 'D1'), ('2', 'D2')], default='1', max_length=1)),
                ('expires_on', models.DateField()),
                ('description', models.CharField(blank=True, max_length=100, null=True)),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='documents', to='account.StaffProfile')),
            ],
        ),
        migrations.CreateModel(
            name='EscortProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_card', models.CharField(blank=True, max_length=100, null=True)),
                ('birthday', models.DateField(blank=True, null=True)),
                ('emergency_number', models.CharField(blank=True, max_length=100, null=True)),
                ('spouse_name', models.CharField(blank=True, max_length=100, null=True)),
                ('spouse_number', models.CharField(blank=True, max_length=100, null=True)),
                ('parent_name', models.CharField(blank=True, max_length=100, null=True)),
                ('parent_number', models.CharField(blank=True, max_length=100, null=True)),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
                ('status', models.CharField(choices=[('A', 'Available'), ('W', 'In Work')], default='A', max_length=1)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='escort_profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DriverProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_card', models.CharField(blank=True, max_length=100, null=True)),
                ('birthday', models.DateField(blank=True, null=True)),
                ('emergency_number', models.CharField(blank=True, max_length=100, null=True)),
                ('spouse_name', models.CharField(blank=True, max_length=100, null=True)),
                ('spouse_number', models.CharField(blank=True, max_length=100, null=True)),
                ('parent_name', models.CharField(blank=True, max_length=100, null=True)),
                ('parent_number', models.CharField(blank=True, max_length=100, null=True)),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
                ('status', models.CharField(choices=[('A', 'Available'), ('W', 'In Work')], default='A', max_length=1)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='driver_profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CustomerProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('contact', models.CharField(max_length=100)),
                ('mobile', models.CharField(max_length=30)),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
                ('product_characteristics', models.CharField(blank=True, max_length=100, null=True)),
                ('payment_method', models.CharField(choices=[('T', '吨'), ('D', '吨/公里'), ('P', '一口价')], default='T', max_length=1)),
                ('customer_request', models.TextField(blank=True, null=True)),
                ('associated_with', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='customers', to='account.StaffProfile')),
                ('products', models.ManyToManyField(to='info.Product')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='customer_profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-updated'],
            },
        ),
    ]
