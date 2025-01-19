from django.db import models

# Create your models here.

class TeamPlayer(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    runs = models.IntegerField()
    balls = models.IntegerField()
