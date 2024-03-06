from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('about/', views.about),
    path('resume/', views.resume),
    path('services/', views.services),
    path('contact/', views.contact)
]
