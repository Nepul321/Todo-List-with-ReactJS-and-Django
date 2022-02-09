from unicodedata import name
from .views import (
  APIBaseView
)

from django.urls import path

urlpatterns = [
    path('', APIBaseView, name="api-base"),
]
