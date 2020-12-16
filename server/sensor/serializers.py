from rest_framework import serializers
from .models import *

class HomeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Home
        fields='__all__'


class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Sensor
        fields='__all__'


class PSPSerializer(serializers.ModelSerializer):
    class Meta:
        model=ContactPSP
        fields='__all__'
