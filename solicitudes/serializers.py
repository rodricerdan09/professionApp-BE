from rest_framework import serializers
from .models import Entidad

# class EntidadSerializer(serializers.Serializer):
#     pk = serializers.IntegerField(read_only=True)
#     nombre = serializers.CharField(max_length=50)
#     provincia = serializers.IntegerField()
#
#     def create(self, validated_data):
#         return Entidad.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.nombre = validated_data.get('nombre', instance.nombre)
#         instance.provincia = validated_data.get('provincia', instance.provincia)
#         instance.save()
#         return instance


class EntidadSerializer(serializers.ModelSerializer):

    class Meta:
        model = Entidad
        fields = ('id', 'nombre', 'provincia')
