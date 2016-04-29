from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class UserProfile(AbstractUser):
    group = models.CharField(max_length=20, verbose_name="Группа")
    telephone = models.CharField(max_length=12, verbose_name="Телефон", null=True, default="")