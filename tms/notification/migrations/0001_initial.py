# Generated by Django 2.2.1 on 2019-06-22 18:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('msg_type', models.PositiveIntegerField(choices=[(0, 'Job Notification'), (1, 'Enter Area Notification'), (2, 'Exit Area Notification'), (2, 'Black Dot Notification')], default=0)),
                ('message', models.TextField()),
                ('is_read', models.BooleanField(default=False)),
                ('sent_on', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notifications', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('is_read', '-sent_on'),
            },
        ),
    ]
