from rest_framework.generics import ListCreateAPIView
from rest_framework.pagination import CursorPagination
from django_filters.rest_framework import DjangoFilterBackend


from races import models as races_models
from races import serializers as races_serializers


class TicketsPagination(CursorPagination):
    page_size = 5
    ordering = '-created_at'


class ListCreateTickets(ListCreateAPIView):
    queryset = races_models.Ticket.objects.all()
    serializer_class = races_serializers.TicketSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = (
        'event_id', 'race_id', 'ticket_id'
    )
    pagination_class = TicketsPagination
