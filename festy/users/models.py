from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import uuid


# To add more fields if necessary later
# class Participant(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     #p_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     #p_name = models.CharField(max_length=100)
#     #email = models.EmailField()

# @receiver(post_save, sender=User)
# def create_user(sender, instance, created, **kwargs):
#     if created:
#         Participant.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def save_user(sender, instance, **kwargs):
#     instance.participant.save()