import django_filters
from .models import Profesional


class ProfesionalFilter(django_filters.FilterSet):
    class Meta:
        model = Profesional
        fields = ('profesion', 'servicio')

