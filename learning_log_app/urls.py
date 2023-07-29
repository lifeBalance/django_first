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
    # Individual Topic pages (pages that focus on a single topic).
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    # Page for adding a new topic.
    path('new_topic/', views.new_topic, name='new_topic'),
    # Page for adding a new entry. When the server receives a request against
    # 'new_entry/<int:topic_id>/', Django sends the requested topic number as
    # an integer to the new_entry view function, in a variable named 'topic_id'.
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
]