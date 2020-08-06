from rest_framework import generics, viewsets
from .serializers import ProfesionSerializer, EspecialidadSerializer
from .models import Profesion, Especialidad


class ProfesionList(generics.ListAPIView):
    """
    Retorna un listado de todas las profesiones
    """
    queryset = Profesion.objects.all()
    serializer_class = ProfesionSerializer


class ProfesionDetail(generics.RetrieveAPIView):
    """
    Retorna los detalles de una profesion
    """
    queryset = Profesion.objects.all()
    serializer_class = ProfesionSerializer


class EspecialidadList(generics.ListAPIView):
    """
    Retorna todas las Especialidades de una Profesion
    """

    def get_queryset(self):
        queryset = Especialidad.objects.filter(profesion_id=self.kwargs["pk"])
        return queryset
    serializer_class = EspecialidadSerializer


class ProfesionEspecialidadDetail(generics.RetrieveAPIView):
    """
    Retorna los detalles de una Especialdiad a partir de una Profesion
    """
    # queryset = Especialidad.objects.all()
    def get_queryset(self):
        queryset = Especialidad.objects.filter(profesion_id=self.kwargs["profesion_pk"]).filter(id=self.kwargs["pk"])
        return queryset
    serializer_class = EspecialidadSerializer


class EspecialidadDetail(generics.RetrieveAPIView):
    """
    Retorna los detalles de una Especialidad
    """
    queryset = Especialidad.objects.all()
    serializer_class = EspecialidadSerializer
