# Generated by Django 4.1.6 on 2023-02-07 04:57

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Event",
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
                ("event_name", models.CharField(max_length=100)),
                ("description", models.TextField()),
                ("event_start_timestamp", models.DateTimeField()),
                ("event_end_timestamp", models.DateTimeField()),
                (
                    "event_location_lon",
                    models.DecimalField(decimal_places=6, max_digits=8),
                ),
                (
                    "event_location_lat",
                    models.DecimalField(decimal_places=6, max_digits=8),
                ),
                ("event_capacity", models.IntegerField()),
                ("event_joinees", models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
