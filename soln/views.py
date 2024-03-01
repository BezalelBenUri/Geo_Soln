from rest_framework import viewsets
# Create your views here.
from .models import HealthFacilities
from .serializers import HealthFacilitiesSerializer

class HealthFacilitiesViewSet(viewsets.ModelViewSet):
    queryset = HealthFacilities.objects.all()
    serializer_class = HealthFacilitiesSerializer
