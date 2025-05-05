from django.contrib import admin
from django.urls import path, include
from app.views import *
from app import views

urlpatterns = [
    path('', include('app.urls')),
]
    