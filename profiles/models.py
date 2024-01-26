from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

STATUS_CHOICES = [
  ('Ink Slinger', 'Ink Slinger'),
  ('Ink Addict', 'Ink Addict'),
  ('Looking for Inspo', 'Looking for Inspo'),
]

class Profile(models.Model):
  owner = models.OneToOneField(User, on_delete=models.CASCADE)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now_add=True)
  name = models.CharField(max_length=255, blank=True)
  bio = models.TextField(blank=True)
  status = models.CharField(max_length=50, choices=STATUS_CHOICES, blank=True)
  image = models.ImageField(
    upload_to='images/',
    default='../default_profile'
  )

  class Meta:
    ordering = ['-created_at']

  def __str__(self):
    return f"{self.owner} - {self.status}"


def create_profile(sender, instance, created, **kwargs):
  if created:
    Profile.objects.create(owner=instance)

post_save.connect(create_profile, sender=User)