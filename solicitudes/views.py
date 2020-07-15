from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import status
from .models import Entidad
from .serializers import EntidadSerializer


class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


@csrf_exempt
def entidad_list(request):
    if request.method == 'GET':
        entidades = Entidad.objects.all()
        entidades_serializer = EntidadSerializer(entidades, many=True)
        return JSONResponse(entidades_serializer.data)
    elif request.method == 'POST':
        entidad_data = JSONParser().parse(request)
        entidad_serializer = EntidadSerializer(data=entidad_data)
        if entidad_serializer.is_valid():
            entidad_serializer.save()
            print("hice un POST")
            return JSONResponse(entidad_serializer.data, status=status.HTTP_201_CREATED)

        return JSONResponse(entidad_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
def entidad_detail(request, pk):
    try:
        entidad = Entidad.objects.get(pk=pk)
    except Entidad.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        entidad_serializer = EntidadSerializer(entidad)
        print("hice un GET")
        return JSONResponse(entidad_serializer.data)

    elif request.method == 'PUT':
        print("hice un PUT")
        entidad_data = JSONParser().parse(request)
        entidad_serializer = EntidadSerializer(entidad, data=entidad_data)
        if entidad_serializer.is_valid():
            entidad_serializer.save()
            return JSONResponse(entidad_serializer.data)
        return JSONResponse(entidad_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        print("hice un DELETE")
        entidad.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)