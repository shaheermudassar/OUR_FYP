from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from .models import UserStats

# Signal to create UserStats when a new user is created
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_user_stats(sender, instance, created, **kwargs):
    if created:
        UserStats.objects.create(user=instance)

# Signal to save UserStats when the user is updated
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def save_user_stats(sender, instance, **kwargs):
    if hasattr(instance, 'userstats'):
        instance.userstats.save()
