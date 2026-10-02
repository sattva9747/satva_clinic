from rest_framework import serializers
from .models import Appointment


class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = [
            "id",
            "appointment_date",
            "appointment_time",
            "description",
            "status",
            "created_at",
            "updated_at",
        ]
