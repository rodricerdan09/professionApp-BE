from django.views.generic import ListView, DetailView, UpdateView
from .models import Solicitud, Entidad, UsuarioErp


class SolicitudListView(ListView):
    model = Solicitud
    # paginate_by = 10


class SolicitudDetailView(DetailView):
    model = Solicitud


class SolicitudUpdateView(UpdateView):
    model = Solicitud


class EntidadDetailView(DetailView):
    model = Entidad
    template_name = 'solicitudes/entidad_detail.html'


class UsuarioErpDetailView(DetailView):
    model = UsuarioErp