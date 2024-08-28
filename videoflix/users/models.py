from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    custom = models.CharField(max_length=100, blank=True, null=True, default="")
    phone = models.CharField(max_length=20, blank=True, null=True, default="")
    adress = models.CharField(max_length=100, blank=True, null=True, default="")