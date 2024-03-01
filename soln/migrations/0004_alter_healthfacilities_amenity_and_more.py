# Generated by Django 5.0.1 on 2024-02-23 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("soln", "0003_healthfacilities_geom_index"),
    ]

    operations = [
        migrations.AlterField(
            model_name="healthfacilities",
            name="amenity",
            field=models.CharField(max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name="healthfacilities",
            name="healthcare",
            field=models.CharField(max_length=167, null=True),
        ),
        migrations.AlterField(
            model_name="healthfacilities",
            name="name",
            field=models.CharField(max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name="healthfacilities",
            name="operatorty",
            field=models.CharField(max_length=80, null=True),
        ),
    ]
