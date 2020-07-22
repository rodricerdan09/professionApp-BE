from rest_framework import serializers
from .models import Profesion, Especialidad


class EspecialidadSerializer(serializers.HyperlinkedModelSerializer):
    profesion = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='profesion_detail')

    class Meta:
        model = Especialidad
        fields = (
            'pk',
            'id',
            'nombre',
            'profesion')


class ProfesionSerializer(serializers.HyperlinkedModelSerializer):
    especialidades = serializers.SlugRelatedField(
        queryset=Especialidad.objects.all(),
        slug_field='nombre'
    )

    class Meta:
        model = Profesion
        fields = '__all__'
