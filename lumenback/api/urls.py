from django.urls import path
from . import views
from api.convert import run_only_once

urlpatterns = [
    path('processFile/', views.processFile, name='processFile')
]
