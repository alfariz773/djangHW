from django.db import models

class details(models.Model):
    name= models.CharField(max_length=100)
    email= models.EmailField()
    phone= models.CharField(max_length=12)
