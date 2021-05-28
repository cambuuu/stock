from django.shortcuts import render
from rest_framework.response import Response
from .models import Productos
from .serializers import ProductosSerializers
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET'])
def ProductosLista(request):
    productos = Productos.objects.all()
    serializer = ProductosSerializers(productos, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def ProductosDetalle(request, pk):
    productos = Productos.objects.get(id=pk)
    serializer = ProductosSerializers(productos, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def ProductosActualizar(request, pk):
    productos = Productos.objects.get(id=pk)
    serializer = ProductosSerializers(instance=productos, data=request.data)
    if serializer.is_valid():
        serializer.save()
    else:
        return Response(serializer.errors)
    return Response(serializer.data)

@api_view(['POST'])
def ProductosCrear(request):
    serializer = ProductosSerializers(data= request.data)
    if serializer.is_valid():
        serializer.save()
    else:
        return Response(serializer.errors)
    return Response(serializer.data)

@api_view(['DELETE'])
def ProductosEliminar(request, pk):
    productos = Productos.objects.get(id=pk)
    productos.delete()

    return Response('Eliminado')