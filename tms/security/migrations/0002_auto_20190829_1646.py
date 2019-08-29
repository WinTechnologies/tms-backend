# Generated by Django 2.2.1 on 2019-08-29 08:46

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('security', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestQuestionResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_correct', models.BooleanField(blank=True, null=True)),
                ('answers', django.contrib.postgres.fields.ArrayField(base_field=models.PositiveIntegerField(), size=None)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='security.Question')),
            ],
        ),
        migrations.AlterField(
            model_name='testresult',
            name='questions',
            field=models.ManyToManyField(through='security.TestQuestionResult', to='security.Question'),
        ),
        migrations.DeleteModel(
            name='TestResultQuestion',
        ),
        migrations.AddField(
            model_name='testquestionresult',
            name='test_result',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='security.TestResult'),
        ),
    ]
