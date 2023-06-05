from django.core.management.base import BaseCommand

from races import models as races_models


class Command(BaseCommand):
    """Clear start list tickets from DB"""

    def handle(self, *args, **options):
        deleted, _ = races_models.Ticket.objects.all().delete()
        print(f'Deleted all {deleted} tickets from the DB')