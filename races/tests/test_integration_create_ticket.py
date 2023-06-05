from django.utils import timezone
from unittest.mock import patch

from django.test import Client, TestCase
from django.urls import reverse

from races import models as races_models


class TestCreatTicket(TestCase):
    """
    Test creating a ticket via the REST API
    """

    def test_create_ticket(self):
        """
        POST to the ticket endpoint with correct data should create a new ticket,
        with its created and update timestamps matching the time the request is received.
        """
        request_data = {
            'event_id': 'e000',
            'race_id': 'r001',
            'ticket_id': 't002',
            'event_title': 'Great Scottish Run',
            'race_title': '10k',
            'ticket_title': 'Standard Ticket',
            'first_name': 'Michael',
            'last_name': 'Kilian',
            'email': 'fake@notreal.com',
        }
        client = Client()

        # Have timezone return a mocked value for 'now'
        test_timestamp = timezone.now()
        with patch('django.utils.timezone.now', lambda: test_timestamp):
            response = client.post(reverse('races:tickets'), request_data)

        self.assertEqual(201, response.status_code)  # HTTP CREATED

        tickets = races_models.Ticket.objects.all()
        self.assertEqual(1, len(tickets))
        ticket = tickets[0]

        # Check created_at and updated_at match and are the expected value
        self.assertEqual(ticket.created_at, ticket.updated_at)
        self.assertEqual(ticket.created_at, test_timestamp)
