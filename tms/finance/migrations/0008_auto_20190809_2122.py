# Generated by Django 2.2.1 on 2019-08-09 13:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0007_auto_20190809_1828'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fuelcard',
            old_name='is_master',
            new_name='is_child',
        ),
    ]
