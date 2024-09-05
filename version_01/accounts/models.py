from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    pass

    def __str__(self):
        return self.email


class Note(models.Model):
    name = models.CharField(null=False, default='', max_length=255)
    body = models.TextField(null=False, default='')

