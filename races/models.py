from django.db import models


class Ticket(models.Model):
    """
    Basic model for an individuals ticket to a race
    """
    # Not to be confused with the primary key - used to track back to original dataset
    dataset_id = models.IntegerField(unique=True, null=True)

    event_id = models.CharField(max_length=8)
    race_id = models.CharField(max_length=8)
    ticket_id = models.CharField(max_length=8)

    created_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(null=True)

    event_title = models.TextField()
    race_title = models.TextField()
    ticket_title = models.TextField()

    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    email = models.EmailField()
