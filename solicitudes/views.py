from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Entidad
from .serializers import EntidadSerializer


@api_view(['GET', 'POST'])
def entidad_list(request):
    """
    Retorna un listado de todas las Entidades
    :param request: POST
    :param pk:
    :return:
    """
    if request.method == 'GET':
        entidades = Entidad.objects.all()
        entidades_serializer = EntidadSerializer(entidades, many=True)
        return Response(entidades_serializer.data)
    elif request.method == 'POST':
        entidad_serializer = EntidadSerializer(data=request.data)

        if entidad_serializer.is_valid():
            entidad_serializer.save()
            print("hice un POST")
            return Response(entidad_serializer.data, status=status.HTTP_201_CREATED)

        return Response(entidad_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def entidad_detail(request, pk):
    """
    Retorna los detalles de una Entidad
    """
    try:
        entidad = Entidad.objects.get(pk=pk)
    except Entidad.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        entidad_serializer = EntidadSerializer(entidad)
        print("hice un GET")
        return Response(entidad_serializer.data)

    elif request.method == 'PUT':
        print("hice un PUT")
        entidad_serializer = EntidadSerializer(entidad, data=request.data)
        if entidad_serializer.is_valid():
            entidad_serializer.save()
            return Response(entidad_serializer.data)
        return Response(entidad_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        print("hice un DELETE")
        entidad.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
