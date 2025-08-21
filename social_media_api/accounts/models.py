from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='static/profile_pics/', blank=True, null=True)
    followers = models.ManyToManyField('self', symmetrical=False, related_name='viewing', blank=True)
    
      # following: users this user follows
    following = models.ManyToManyField(
        'self',
        symmetrical=False,
        related_name='viewers',
        blank=True
    )
    
    
    def __str__(self):
        return self.username