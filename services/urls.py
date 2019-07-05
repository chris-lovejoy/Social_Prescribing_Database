from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:service_id>/', views.detail, name='detail'),
    path('<int:service_id>/recent/', views.recent, name='recent'),
    path('<int:service_id>/location/', views.location, name='location'),
]