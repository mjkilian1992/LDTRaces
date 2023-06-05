from django.utils import timezone
from rest_framework.serializers import ModelSerializer

from races import models as races_models


class TicketSerializer(ModelSerializer):

    class Meta:
        model = races_models.Ticket
        exclude = ['dataset_id']
        read_only_fields = ['created_at', 'updated_at']

    def create(self, validated_data):
        ticket = races_models.Ticket(**validated_data)
        ticket.created_at = timezone.now()
        ticket.updated_at = timezone.now()
        ticket.save()
        return ticket
