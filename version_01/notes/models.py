from django.db import models


class Note(models.Model):
    name = models.CharField(null=False, default='', max_length=255)
    body = models.TextField(null=False, default='')
