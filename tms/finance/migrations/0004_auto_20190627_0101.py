# Generated by Django 2.2.1 on 2019-06-27 01:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0003_auto_20190625_2228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='billdocument',
            name='category',
            field=models.PositiveIntegerField(choices=[(0, 'Bill from Loading Station'), (1, 'Bill from Quality Station'), (2, 'Bill from UnLoading Station'), (3, '加油'), (4, '路票'), (5, '其他')]),
        ),
    ]
