from django.db import models


class Account(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)
    content = models.TextField(max_length=1000, null=True, blank=True)
