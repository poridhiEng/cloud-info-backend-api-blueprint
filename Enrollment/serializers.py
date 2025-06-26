from rest_framework import serializers
from .models import Enrollment  # adjust import based on your project

class EnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        fields = '__all__'  # <-- This is required
        # Do not define read_only_fields here since we're handling it dynamically


    def update(self, instance, validated_data):
        # Remove protected fields even if they're passed
        for field in ['user_id', 'username', 'email']:
            validated_data.pop(field, None)
        return super().update(instance, validated_data)