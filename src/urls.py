from unicodedata import name
from django.contrib import admin
from django.urls import path, include
from .views import (
    HomeView,
    TodoView
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('base.urls')),
    path('', HomeView, name="home"),
    path('todo/<int:id>/', TodoView, name="todo")
]
