# Generated by Django 2.1.7 on 2019-03-24 09:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('currency_exchange', '0011_yyy_task_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='yyy',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 24, 11, 37, 55, 445765)),
        ),
        migrations.AddField(
            model_name='yyy',
            name='hours',
            field=models.DecimalField(decimal_places=12, default=0, max_digits=24),
        ),
        migrations.AddField(
            model_name='yyy',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 24, 11, 37, 55, 445765)),
        ),
        migrations.AddField(
            model_name='yyy',
            name='status',
            field=models.CharField(default='in progress', max_length=100),
        ),
        migrations.AddField(
            model_name='yyy',
            name='task_description',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='yyy',
            name='task_name',
            field=models.CharField(default='', max_length=200),
        ),
    ]
