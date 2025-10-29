from django.db import models
class Std(models.Model):
    Name = models.CharField(max_length=50)
    standard = models.CharField(max_length=50)
    age = models.IntegerField()
