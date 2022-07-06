from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('profile/add/', views.add_track, name='add_track'),
    path('playlist/<slug:slug>/', views.PlaylistDetailView.as_view(), name='playlist'),
    path('profile/add/drumKit', views.add_drumKit, name='drumKit'),
    path('delete/<str:pk>/', views.deleteTrack, name='deleteTrack'),
    path('tracks/', views.tracks, name='allTrack'),
]
