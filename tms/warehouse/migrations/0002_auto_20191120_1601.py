# Generated by Django 2.2.1 on 2019-11-20 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='intransaction',
            name='ticket_type',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='warehouseproduct',
            name='amount_unit',
            field=models.CharField(max_length=100),
        ),
    ]
