# Generated by Django 3.1.2 on 2020-11-11 12:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_driver_car_max_load'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='driver',
            name='current_location',
        ),
    ]