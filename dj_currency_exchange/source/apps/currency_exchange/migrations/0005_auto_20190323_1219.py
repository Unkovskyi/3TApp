# Generated by Django 2.1.7 on 2019-03-23 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('currency_exchange', '0004_auto_20190323_1206'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('code', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('estimation_hours', models.DecimalField(decimal_places=12, max_digits=24)),
            ],
            options={
                'verbose_name': 'Project',
                'verbose_name_plural': 'Projects',
                'db_table': 'projects',
            },
        ),
        migrations.AlterModelTable(
            name='tasks',
            table='tasks',
        ),
    ]
