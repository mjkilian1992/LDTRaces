from django.db import models


class Ticket(models.Model):
    """
    Basic model for an individuals ticket to a race
    """
    eventID = models.CharField(max_length=8)
    raceID = models.CharField(max_length=8)
    ticketID = models.CharField(max_length=8)
    eventTitle = models.TextField()
    raceTitle = models.TextField()
    ticketTitle = models.TextField()
    firstName = models.CharField(max_length=32)
    lastName = models.CharField(max_length=32)
    email = models.EmailField()
