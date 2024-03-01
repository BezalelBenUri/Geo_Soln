from rest_framework.routers import DefaultRouter

from .views import HealthFacilitiesViewSet

router = DefaultRouter()

router.register(
    prefix = "api/v1/geo_soln",
    viewset = HealthFacilitiesViewSet,
    basename = "healthfacilities"
)

urlpatterns = router.urls