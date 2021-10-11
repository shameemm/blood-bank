from django.db import models

# Create your models here.
class Details(models.Model):
    
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    place = models.CharField(max_length=100)
    phone = models.BigIntegerField()
    bgrp = models.CharField(max_length=10)