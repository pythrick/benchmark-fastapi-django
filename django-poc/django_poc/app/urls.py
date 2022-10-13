from rest_framework import routers
from django_poc.app.views import BenchmarkViewSet


router = routers.DefaultRouter()
router.register(r"benchmarks", BenchmarkViewSet)
