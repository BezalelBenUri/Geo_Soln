import os

from django.contrib.gis.utils import LayerMapping
from django.contrib.gis.gdal import DataSource

from soln.models import HealthFacilities

# Layer Mapping
healthfacilities_mapping = {
    "name": "name",
    "healthcare": "healthcare",
    "amenity": "amenity",
    "operatorty": "operatorty",
    "geom": "MULTIPOINT",
}


def load_data(verbose = True):
    file = os.getcwd() + "/data/health_facilities.gpkg"
    data = DataSource(file)
    facilities_layer = data[0].name

    facilities_layer_mapping = LayerMapping(
        HealthFacilities, file, healthfacilities_mapping, layer = facilities_layer
    )
    facilities_layer_mapping.save(strict = True, verbose = verbose)
