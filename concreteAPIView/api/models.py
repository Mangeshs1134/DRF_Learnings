from django.db import models

team =[
    ('mi',"MI"),
    ('rcb',"RCB"),
    ('csk',"CSK"),
    ('kkr',"KKR"),
    ('rr',"RR"),
]
# Create your models here.
class MatchLive(models.Model):
    team1 = models.CharField(max_length=50, choices=team)
    team2 = models.CharField(max_length=50, choices=team)
    inning = models.IntegerField(choices=[(1,1),(2,2)])

    def __str__(self):
        return super().__str__()
