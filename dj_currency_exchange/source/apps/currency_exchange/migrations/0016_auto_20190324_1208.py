# Generated by Django 2.1.7 on 2019-03-24 10:08

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('currency_exchange', '0015_tasks'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaskStatus',
            fields=[
                ('code', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'Task Status',
                'verbose_name_plural': 'Task Status',
                'db_table': 'task_status',
            },
        ),
        migrations.AlterField(
            model_name='tasks',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 24, 12, 8, 33, 339786)),
        ),
        migrations.AlterField(
            model_name='tasks',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 24, 12, 8, 33, 339786)),
        ),
        migrations.AlterField(
            model_name='tasks',
            name='status',
            field=models.ForeignKey(default='in progress', on_delete=django.db.models.deletion.CASCADE, to='currency_exchange.TaskStatus'),
        ),
    ]
