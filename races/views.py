from rest_framework.generics import ListCreateAPIView
from django_filters.rest_framework import DjangoFilterBackend


from races import models as races_models
from races import serializers as races_serializers


class ListCreateTickets(ListCreateAPIView):
    queryset = races_models.Ticket.objects.all()
    serializer_class = races_serializers.TicketSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = (
        'event_id', 'race_id', 'ticket_id'
    )
