from django_poc.app.models import Benchmark
from rest_framework import serializers


class BenchmarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Benchmark
        fields = "__all__"
