# Generated by Django 3.1.2 on 2020-11-16 15:41

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20201111_1249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver',
            name='current_location',
            field=django.contrib.gis.db.models.fields.PointField(default=None, null=True, srid=4326),
        ),
    ]
