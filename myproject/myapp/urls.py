from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('contact/', views.contact),
    path('form/', views.form, name='form'),
]