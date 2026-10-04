from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import PatientQuestion
from .serializers import PatientQuestionSerializer


class PatientQuestionListCreateView(generics.ListCreateAPIView):
    serializer_class = PatientQuestionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return PatientQuestion.objects.filter(patient=self.request.user)

    def perform_create(self, serializer):
        serializer.save(patient=self.request.user)

