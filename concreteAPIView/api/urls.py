from django.urls import path
from . import views

urlpatterns = [
    path('matchlive', views.MatchLiveList.as_view() ),
    path('matchlive/<int:pk>', views.MatchLiveDetail.as_view() ),
    path('matchlive/create/', views.MatchLiveCreate.as_view() ),
    path('matchlive/create/<int:pk>', views.MatchLiveUpdate.as_view() ),
    path('matchlive/delete/<int:pk>', views.MatchLiveDelete.as_view() ),
]