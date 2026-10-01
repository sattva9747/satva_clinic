from rest_framework import generics
from .models import Therapist
from .serializers import TherapistSerializer


class TherapistListView(generics.ListAPIView):
    queryset = Therapist.objects.filter(active=True)
    serializer_class = TherapistSerializer


class TherapistDetailView(generics.RetrieveAPIView):
    queryset = Therapist.objects.filter(active=True)
    serializer_class = TherapistSerializer


