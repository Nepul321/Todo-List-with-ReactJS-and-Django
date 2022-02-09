from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import (
    Todo
)

from .serializers import TodoSerializer

@api_view(['GET'])
def APIBaseView(request):
    return Response("API BASE POINT", status=200)

@api_view(['GET'])
def TodosListView(request):
    qs = Todo.objects.filter(completed=False)
    serializer = TodoSerializer(qs, many=True)
    data = serializer.data
    return Response(data, status=200)