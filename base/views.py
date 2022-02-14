from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import (
    Todo
)

from .serializers import TodoSerializer

@api_view(['GET'])
def APIBaseView(request):
    return Response("API BASE POINT", status=200)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def TodosListView(request):
    context = {"request" : request}
    qs = Todo.objects.filter(user=request.user)
    serializer = TodoSerializer(qs, many=True, context=context)
    data = serializer.data
    return Response(data, status=200)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def TodosDetailView(request, id):
    context = {"request" : request}
    qs = Todo.objects.filter(id=id)
    if not qs:
        return Response({"detail" : "Todo not found"}, status=404)
    obj = qs.first()
    if obj.user != request.user:
        return Response({"detail" : "Access denied"}, status=403)
    serializer = TodoSerializer(obj, context=context)
    data = serializer.data
    return Response(data, status=200)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def TodosUpdateView(request, id):
    context = {"request" : request}
    data = request.data
    qs = Todo.objects.filter(id=id)
    if not qs:
        return Response({"detail" : "Todo not found"}, status=404)
    obj = qs.first()
    if obj.user != request.user:
        return Response({"detail" : "Access denied"}, status=403)    
    serializer = TodoSerializer(instance=obj, data=data, context=context)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        data = serializer.data
        return Response(data, status=200)
    return Response({}, status=401)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def TodosDeleteView(request, id):
    context = {"request" : request}
    qs = Todo.objects.filter(id=id)
    if not qs:
        return Response({"detail" : "Todo not found"}, status=404)

    obj = qs.first()

    if obj.user != request.user:
        return Response({"detail" : "Access denied"}, status=403)

    obj.delete()
    return Response({"detail" : "Todo deleted"}, status=200)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def TodosCreateView(request):
    context = {"request" : request}
    data = request.data
    serializer = TodoSerializer(data=data, context=context)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user)
        data = serializer.data
        return Response(data, status=201)
    return Response({}, status=401)
