# Generated by Django 4.2.2 on 2023-06-05 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Ticket",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("eventID", models.CharField(max_length=8)),
                ("raceID", models.CharField(max_length=8)),
                ("ticketID", models.CharField(max_length=8)),
                ("eventTitle", models.TextField()),
                ("raceTitle", models.TextField()),
                ("ticketTitle", models.TextField()),
                ("firstName", models.CharField(max_length=32)),
                ("lastName", models.CharField(max_length=32)),
                ("email", models.EmailField(max_length=254)),
            ],
        ),
    ]
