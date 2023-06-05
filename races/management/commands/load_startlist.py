import json

from django.core.management.base import BaseCommand

from races import models as races_models


def load_race_data( filepath: str) -> dict:
    with open(filepath, 'r') as jsonfile:
        as_json = json.load(jsonfile)
    return as_json


def flatten_fields_to_dict(fields: list) -> dict:
    """
    Convert the fields format of the JSON dataset to a standard dict structure, where the field name
    is the key
    """
    return {entry['id']: entry['value'] for entry in fields}


class Command(BaseCommand):
    """Load startlist data from JSON"""

    def add_arguments(self, parser):
        parser.add_argument('filepath', nargs=1, type=str)

    def handle(self, *args, **options):
        filepath = options['filepath'][0]
        loaded_json = load_race_data(filepath)
        for ticket in loaded_json:
            fields = flatten_fields_to_dict(ticket['fields'])
            try:
                races_models.Ticket.objects.create(
                    dataset_id=ticket['id'],
                    event_id=ticket['eventId'],
                    race_id=ticket['raceId'],
                    ticket_id=ticket['ticketId'],
                    event_title=ticket['eventTitle'],
                    first_name=fields['firstName'],
                    last_name=fields['lastName'],
                    email=fields['emailAddress'],
                )
            except Exception as e:
                print(f'Error adding entry ID {ticket["id"]} - {e}')