from django.contrib.auth.models import User
from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=255)
    user = models.ForeignKey(User, blank=True, on_delete=models.CASCADE, null=True)
    completed = models.BooleanField(default=False)
    datetime = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-datetime']