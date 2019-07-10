# Generated by Django 2.2.1 on 2019-07-10 19:36

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
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('path', django.contrib.postgres.fields.ArrayField(base_field=models.PositiveIntegerField(), size=18)),
                ('policy', models.PositiveIntegerField(choices=[(0, '最快捷模式'), (1, '最经济模式'), (2, '最短距离模式')], default=0)),
                ('distance', models.PositiveIntegerField()),
            ],
            options={
                'ordering': ('-updated',),
                'abstract': False,
            },
        ),
    ]
