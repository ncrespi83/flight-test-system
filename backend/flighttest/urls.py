from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import RequirementViewSet, TestPointViewSet, TestEventViewSet, TestPlanViewSet

router = DefaultRouter()
router.register(r"requirements", RequirementViewSet, basename = "requirement")
router.register(r"testpoints", TestPointViewSet, basename = "testpoint")
router.register(r"testevents", TestEventViewSet, basename = "testevent")
router.register(r"testplans", TestPlanViewSet, basename = "testplan")

urlpatterns = [
    path("", include(router.urls)),
]