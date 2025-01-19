from django.contrib import admin
from .models import TeamPlayer

# Register your models here.
@admin.register(TeamPlayer)
class TeamPlayerAdmin(admin.ModelAdmin):
    list_display = ['name', 'age', 'runs', 'balls']
