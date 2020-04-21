from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.

class Rides(models.Model):
    depDate = models.DateField()
    depTime = models.TimeField()
    depZip = models.IntegerField()
    arrZip = models.IntegerField()
    driEmail = models.EmailField()
    reserved = models.TextField(default='Open')
    
    def __str__(self):
        return self.depDate
        
    