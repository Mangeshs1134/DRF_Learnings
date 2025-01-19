from . import views
from django.urls import path, include
from rest_framework import routers

router = routers.DefaultRouter() 
# router.register('TeamPlayer', views.TeamPlayerViewSet)
router.register(r'teamplayer', views.TeamPlayerViewSet)

urlpatterns = [
    path('', include(router.urls) ),
] 
