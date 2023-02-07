from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.
class Event(models.Model):
    # title = models.CharField(max_length=100)
    #event_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    event_name = models.CharField(max_length=100)
    description = models.TextField()
    event_start_timestamp = models.DateTimeField()
    event_end_timestamp = models.DateTimeField()
    event_location_lon = models.DecimalField(max_digits=8, decimal_places=6)
    event_location_lat = models.DecimalField(max_digits=8, decimal_places=6) 
    event_capacity = models.IntegerField()
    event_joinees = models.ManyToManyField(User)
