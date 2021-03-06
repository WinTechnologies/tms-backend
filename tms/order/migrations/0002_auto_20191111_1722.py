# Generated by Django 2.2.1 on 2019-11-11 17:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='jobworker',
            options={'ordering': ('job', '-active', '-assigned_on')},
        ),
        migrations.AlterModelOptions(
            name='orderpayment',
            options={'ordering': ('-updated',)},
        ),
        migrations.AddField(
            model_name='jobworker',
            name='active',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='orderpayment',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='orderpayment',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
