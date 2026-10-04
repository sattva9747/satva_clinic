from rest_framework import serializers
from .models import PatientQuestion


class PatientQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientQuestion
        fields = [
            "id",
            "patient",
            "question",
            "answer",
            "created_at",
            "answered_at",
        ]
        read_only_fields = [
            "id",
            "patient",
            "answer",
            "created_at",
            "answered_at",
        ]