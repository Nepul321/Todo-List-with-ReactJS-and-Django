from .views import (
  APIBaseView,
  TodosListView,
  TodosDetailView,
  TodosUpdateView,
  TodosDeleteView
)

from django.urls import path

urlpatterns = [
    path('', APIBaseView, name="api-base"),
    path('todos/', TodosListView, name="todos-list-view"),
    path('todos/<int:id>/', TodosDetailView, name="todos-detail-view"),
    path('todos/<int:id>/update/', TodosUpdateView, name="todos-update-view"),
    path('todos/<int:id>/delete/', TodosDeleteView, name="todos-delete-view"),
]
