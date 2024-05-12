from django.db import models
from datetime import time

class Club(models.Model):
    name = models.CharField(max_length=200)
    location= models.CharField(max_length=200)
    club_number= models.IntegerField()
    
    def __str__(self):
        return f"{self.name} at {self.club_number} on {self.location}"
    
class Fixture(models.Model):
    title = models.CharField(max_length=200)
    date=models.DateField()
    start_time = models.TimeField(default=time(9))
    duration = models.IntegerField(default=1)
    club = models.ForeignKey(Club, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} at {self.start_time} on {self.date}"
# Create your models here.
