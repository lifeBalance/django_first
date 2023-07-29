"""Defines URL patters for accounts."""

from django.urls import path, include

app_name = 'accounts_app'

urlpatterns = [
    # Include default auth urls
    path('', include('django.contrib.auth.urls'))
]