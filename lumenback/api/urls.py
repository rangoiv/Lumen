from django.urls import path
from . import views

urlpatterns = [
    path('processFile/', views.processFile, name = 'processFile'),
    path('print_trusted_origins/', views.print_trusted_origins, name='print_trusted_origins'),
]
