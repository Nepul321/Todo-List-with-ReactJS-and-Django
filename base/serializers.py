from .models import (
    Todo
)

from rest_framework import serializers

class TodoSerializer(serializers.ModelSerializer):
    is_owner = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Todo
        fields = ('id', 'title', 'completed', 'datetime','is_owner')

    def get_is_owner(self, obj):
        request = self.context['request']
        is_owner = False
        if request.user == obj.user:
            is_owner = True
        return is_owner