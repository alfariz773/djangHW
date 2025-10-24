from django.db import models

class customer(models.Model):
    name = models.CharField( max_length=50)
    email= models.EmailField()
