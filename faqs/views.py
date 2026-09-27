from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from .models import FAQ
from .serializers import FAQSerializer


class FAQView(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request):

        serializer = FAQSerializer(
            data=request.data
        )

        if serializer.is_valid():

            faq = serializer.save(
                patient=request.user
            )

            return Response(
                FAQSerializer(faq).data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def get(self, request):

        faqs = FAQ.objects.filter(
            patient=request.user
        )

        serializer = FAQSerializer(
            faqs,
            many=True
        )

        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )