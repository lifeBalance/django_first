"""Defines URL patterns for learning_log_app."""
from django.urls import path

from . import views

app_name = 'learning_log_app'
urlpatterns = [
    # Home page. The function path takes in 3 arguments:
    # 1. The URL (Base URL is ignored: http://localhost:8000)
    # 2. The module.function with the controller (views.py, index function)
    # 3. A handy name that we can use in links to this route.
    path('', views.index, name='index'),
    # Topics page (list with all topics).
    path('topics/', views.topics, name='topics'),
]