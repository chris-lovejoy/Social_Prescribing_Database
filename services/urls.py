from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('recent', views.recent, name='recent'),
    path('location', views.location, name='location'),
]