from rest_framework import serializers
from .models import Entidad

'''
class Toy(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=150, blank=False, default='')
    description = models.CharField(max_length=250, blank=True, default='')
    toy_category = models.CharField(max_length=200, blank=False,default='')
    release_date = models.DateTimeField()
    was_included_in_home = models.BooleanField(default=False)

class ToySerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=150)
    description = serializers.CharField(max_length=250)
    release_date = serializers.DateTimeField()
    toy_category = serializers.CharField(max_length=200)
    was_included_in_home = serializers.BooleanField(required=False)
'''


class EntidadSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    nombre = serializers.CharField(max_length=50)
    provincia = serializers.IntegerField()

    def create(self, validated_data):
        return Entidad.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.nombre = validated_data.get('nombre', instance.nombre)
        instance.provincia = validated_data.get('provincia', instance.provincia)
        instance.save()
        return instance
