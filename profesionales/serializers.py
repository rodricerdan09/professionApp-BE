from rest_framework import serializers
from .models import Profesion, Especialidad
from solicitudes.serializers import EntidadSerializer


class ProfesionSerializer(serializers.ModelSerializer):
    entidad = EntidadSerializer(many=True, read_only=True)
    # entidad = serializers.PrimaryKeyRelatedField(
    #     queryset=Entidad.objects.all(),
    #     many=True
    # )

    class Meta:
        model = Profesion
        fields = (
            'id',
            'nombre',
            'nombre_corto',
            'entidad'
        )


class EspecialidadSerializer(serializers.ModelSerializer):
    profesion = ProfesionSerializer(many=False, read_only=True)

    class Meta:
        model = Especialidad
        fields = (
            'id',
            'nombre',
            'profesion'
        )
