# Generated by Django 5.0.1 on 2024-02-23 12:55

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("soln", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="healthfacilities",
            name="geom",
            field=django.contrib.gis.db.models.fields.MultiPointField(srid=4326),
        ),
    ]
