# Generated by Django 2.2.1 on 2019-06-19 08:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('info', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='DriverLicense',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('number', models.CharField(max_length=100)),
                ('expires_on', models.DateField()),
                ('document_type', models.CharField(choices=[('1', 'D1'), ('2', 'D2')], default='1', max_length=1)),
                ('description', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'ordering': ['name'],
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
                ('status', models.CharField(choices=[('A', 'Available'), ('N', 'Not Available')], default='A', max_length=1)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hr.Department')),
                ('driver_license', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='hr.DriverLicense')),
                ('position', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='hr.Position')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
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
                ('associated_with', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='customers', to='hr.StaffProfile')),
                ('products', models.ManyToManyField(to='info.Product')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='customer_profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-updated'],
            },
        ),
        migrations.CreateModel(
            name='RoleManagement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('permission', models.PositiveIntegerField(choices=[(0, 'No permission'), (1, 'Read Permission'), (2, 'Write Permission')], default=0)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hr.Department')),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hr.Position')),
            ],
            options={
                'ordering': ['department', 'position'],
                'unique_together': {('department', 'position')},
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
                ('category', models.CharField(max_length=1)),
                ('from_date', models.DateField()),
                ('to_date', models.DateField()),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hr.StaffProfile')),
            ],
            options={
                'unique_together': {('staff', 'from_date', 'to_date')},
            },
        ),
    ]