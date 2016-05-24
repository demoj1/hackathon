from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class UserProfile(AbstractUser):
    group = models.CharField(max_length=20, verbose_name="Группа")
    telephone = models.CharField(max_length=12, verbose_name="Телефон", null=True, default="")


class Report(models.Model):
    user = models.ForeignKey(UserProfile)

    heroku_url = models.CharField(max_length=200, default="", null=False)
    github_url = models.CharField(max_length=200, default="", null=False)

    notes = models.TextField()

    def __str__(self):
        return "Работа участника {}".format(self.user)

    class Meta:
         verbose_name = "Отчет о работе"
         verbose_name_plural = "Отчеты о работе"
