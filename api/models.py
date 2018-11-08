from django.db import models
from django.utils import timezone


class Url(models.Model):
    old_url = models.CharField(max_length=2000)
    new_url = models.CharField(max_length=2000)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.old_url
