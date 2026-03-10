from rest_framework import serializers
from .models import Client
from cards.serializers import CardSerializer


class ClientSerializer(serializers.ModelSerializer):
    client_cards = CardSerializer(many=True)

    class Meta:
        model = Client
        fields = ("id", "first_name", "last_name", "age",
                  "email", "phone", "balance",
                  "avatar", "address", "client_cards"
                  )