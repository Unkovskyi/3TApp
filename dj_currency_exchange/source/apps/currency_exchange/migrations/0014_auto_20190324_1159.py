# Generated by Django 2.1.7 on 2019-03-24 09:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('currency_exchange', '0013_auto_20190324_1150'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Tasks',
        ),
        migrations.RemoveField(
            model_name='yyy',
            name='project',
        ),
        migrations.RemoveField(
            model_name='yyy',
            name='user',
        ),
        migrations.DeleteModel(
            name='YYY',
        ),
    ]