from rest_framework import generics
from .models import Client
from .serializers import ClientSerializer
from rest_framework import permissions


class ClientListAPIView(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [permissions.IsAuthenticated, ]


class ClientRetrieveAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer