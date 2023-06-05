from rest_framework.generics import ListCreateAPIView

from races import models as races_models
from races import serializers as races_serializers


class ListCreateTickets(ListCreateAPIView):
    queryset = races_models.Ticket.objects.all()
    serializer_class = races_serializers.TicketSerializer
