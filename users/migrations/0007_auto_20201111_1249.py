# Generated by Django 3.1.2 on 2020-11-11 12:49

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20201111_1247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver',
            name='current_location',
            field=django.contrib.gis.db.models.fields.PointField(srid=4326),
        ),
    ]
