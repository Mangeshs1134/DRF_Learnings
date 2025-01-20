from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r"todo", views.TodoViewSet, basename='todo' )

urlpatterns = [
    path('', include(router.urls) ),
]
