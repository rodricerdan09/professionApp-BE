from django.forms import ModelForm
from .models import Solicitud


class SolicitudCreationForm(ModelForm):
    class Meta:
        model = Solicitud
        fields = ('entidad', 'estado')
        readonly_fields = ('estado',)
        exclude = ('estado',)