from django.contrib import admin
from django.urls import path
from serializer import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', views.student_detail),
    path('studInfo/<int:roll>', views.student_detail),
    path('studList/', views.student_list),
]
