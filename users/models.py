from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='Email address')
    
    telephone = models.CharField(max_length=20, blank=True, null=True, verbose_name='Telephone')
    city = models.CharField(max_length=100, blank=True, null=True, verbose_name='City')
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True, verbose_name='Avatar')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
