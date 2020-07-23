from rest_framework import generics, viewsets
from .serializers import ProfesionSerializer, EspecialidadSerializer
from .models import Profesion, Especialidad


class ProfesionList(generics.ListAPIView):
    queryset = Profesion.objects.all()
    serializer_class = ProfesionSerializer


class ProfesionDetail(generics.RetrieveAPIView):
    queryset = Profesion.objects.all()
    serializer_class = ProfesionSerializer


class EspecialidadList(generics.ListAPIView):
    """
        sirve para la url api/profesion/2/especialidad
    """

    def get_queryset(self):
        queryset = Especialidad.objects.filter(profesion_id=self.kwargs["pk"])
        return queryset
    serializer_class = EspecialidadSerializer


class ProfesionEspecialidadDetail(generics.RetrieveAPIView):
    """
    sirve para la url api/profesion/2/especialidad/4
    """
    # queryset = Especialidad.objects.all()
    def get_queryset(self):
        queryset = Especialidad.objects.filter(profesion_id=self.kwargs["profesion_pk"]).filter(id=self.kwargs["pk"])
        return queryset
    serializer_class = EspecialidadSerializer


class EspecialidadDetail(generics.RetrieveAPIView):
    """"
    sirve para la url api/especialidad/6
    """
    queryset = Especialidad.objects.all()
    serializer_class = EspecialidadSerializer
