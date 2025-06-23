from .models import PricePlan
from rest_framework import serializers

class PricePlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = PricePlan
        fields = '__all__'