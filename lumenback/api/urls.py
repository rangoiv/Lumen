from django.urls import path
from . import views

urlpatterns = [
    path('processFile/', views.processFile, name = 'processFile')
]
