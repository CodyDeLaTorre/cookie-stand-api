from rest_framework import serializers
from .models import Stand


class StandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stand
        fields = "__all__"
