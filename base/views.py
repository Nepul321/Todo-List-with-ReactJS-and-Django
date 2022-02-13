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
    qs = Todo.objects.all()
    serializer = TodoSerializer(qs, many=True)
    data = serializer.data
    return Response(data, status=200)

@api_view(['GET'])
def TodosDetailView(request, id):
    qs = Todo.objects.filter(id=id)
    if not qs:
        return Response({"detail" : "Todo not found"}, status=404)
    obj = qs.first()
    serializer = TodoSerializer(obj)
    data = serializer.data
    return Response(data, status=200)

@api_view(['POST'])
def TodosUpdateView(request, id):
    data = request.data
    qs = Todo.objects.filter(id=id)
    if not qs:
        return Response({"detail" : "Todo not found"}, status=404)
    obj = qs.first()
    serializer = TodoSerializer(instance=obj, data=data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        data = serializer.data
        return Response(data, status=200)
    return Response({}, status=401)

@api_view(['DELETE'])
def TodosDeleteView(request, id):
    qs = Todo.objects.filter(id=id)
    if not qs:
        return Response({"detail" : "Todo not found"}, status=404)

    obj = qs.first()
    obj.delete()
    return Response({"detail" : "Todo deleted"}, status=200)

@api_view(['POST'])
def TodosCreateView(request):
    data = request.data
    serializer = TodoSerializer(data=data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        data = serializer.data
        return Response(data, status=201)
    return Response({}, status=401)
