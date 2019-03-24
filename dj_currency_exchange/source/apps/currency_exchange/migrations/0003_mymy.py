# Generated by Django 2.1.7 on 2019-03-23 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('currency_exchange', '0002_currency_currencyexchangerate'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyMy',
            fields=[
                ('code', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'MyMy',
                'verbose_name_plural': 'MMMMMMM',
            },
        ),
    ]