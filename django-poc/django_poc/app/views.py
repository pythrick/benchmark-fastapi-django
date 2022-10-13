from django_poc.app.models import Benchmark
from django_poc.app.serializers import BenchmarkSerializer
from rest_framework import viewsets


class BenchmarkViewSet(viewsets.ModelViewSet):
    queryset = Benchmark.objects.all()
    serializer_class = BenchmarkSerializer
