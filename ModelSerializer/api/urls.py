from django.urls import path
from .ClassBasedviews import StudentListAPIView, StudentDetailAPIView
from .views import students, students_detail

urlpatterns = [
    # path('students/', StudentListAPIView.as_view() ),
    # path('students/<int:pk>', StudentDetailAPIView.as_view() ),
    path('students/', students ),
    path('students/<int:pk>', students_detail ),
]
