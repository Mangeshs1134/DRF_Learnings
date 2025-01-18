from django.contrib import admin
from .models import MatchLive

# Register your models here.
@admin.register(MatchLive)
class MatchLiveAdmin(admin.ModelAdmin):
    list_display = ['team1', 'team2', 'inning']

