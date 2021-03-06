# Generated by Django 2.1.7 on 2019-03-24 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('currency_exchange', '0012_auto_20190324_1137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='yyy',
            name='end_time',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='yyy',
            name='hours',
            field=models.DecimalField(decimal_places=12, max_digits=24),
        ),
        migrations.AlterField(
            model_name='yyy',
            name='start_time',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='yyy',
            name='task_description',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='yyy',
            name='task_name',
            field=models.CharField(max_length=200),
        ),
    ]
