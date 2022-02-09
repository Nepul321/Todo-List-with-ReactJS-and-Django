from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)
    datetime = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-datetime']