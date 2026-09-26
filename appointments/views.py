from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from .serializers import AppointmentSerializer
from .models import Appointment


class AppointmentView(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request):

        serializer = AppointmentSerializer(data=request.data)

        if serializer.is_valid():

            appointment = serializer.save(
                patient=request.user
            )

            return Response(
                AppointmentSerializer(appointment).data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def get(self, request):

        appointments = Appointment.objects.filter(
            patient=request.user
        )

        serializer = AppointmentSerializer(
            appointments,
            many=True
        )

        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )