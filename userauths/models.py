from django.db import models
from django.contrib.auth.models import AbstractUser

import uuid
from shortuuid.django_fields import ShortUUIDField

# Create your models here.


class User(AbstractUser):
    username = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)


    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return str(self.username)