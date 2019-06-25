# Generated by Django 2.2.1 on 2019-06-25 16:50

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('path', django.contrib.postgres.fields.ArrayField(base_field=models.PositiveIntegerField(), size=18)),
                ('policy', models.PositiveIntegerField()),
                ('distance', models.PositiveIntegerField()),
            ],
        ),
    ]
