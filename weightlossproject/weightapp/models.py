from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class weightsubmit(models.Model):
    user = models.ForeignKey( User, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
    time = models.TimeField(default=timezone.now)
    weight = models.FloatField()
