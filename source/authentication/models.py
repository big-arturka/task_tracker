from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(verbose_name='Email', max_length=255, unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    first_name = models.CharField(max_length=255, verbose_name='Name')
    profile_image = models.ImageField(default='default_profile_image.jpg', blank=True)
    position = models.CharField(max_length=255)
    telegram_id = models.CharField(max_length=255)

    def __str__(self):
        return self.email


