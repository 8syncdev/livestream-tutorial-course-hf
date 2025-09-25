from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class MyUser(AbstractUser):
    phone = models.CharField(blank=True, max_length=15, verbose_name="user phone")
