# Generated by Django 2.1.7 on 2019-03-23 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('currency_exchange', '0007_auto_20190323_1751'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasks',
            name='hours',
            field=models.DecimalField(decimal_places=12, default=0, max_digits=24),
        ),
        migrations.AddField(
            model_name='tasks',
            name='status',
            field=models.CharField(default='in progress', max_length=100),
        ),
    ]
