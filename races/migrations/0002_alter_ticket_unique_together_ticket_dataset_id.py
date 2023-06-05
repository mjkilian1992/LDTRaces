# Generated by Django 4.2.2 on 2023-06-05 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("races", "0001_initial"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="ticket",
            unique_together=set(),
        ),
        migrations.AddField(
            model_name="ticket",
            name="dataset_id",
            field=models.IntegerField(null=True, unique=True),
        ),
    ]