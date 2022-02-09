from unicodedata import name
from .views import (
  APIBaseView,
  TodosListView
)

from django.urls import path

urlpatterns = [
    path('', APIBaseView, name="api-base"),
    path('todos/', TodosListView, name="todos-list-view")
]
