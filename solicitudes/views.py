from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, UpdateView
from .models import Solicitud, Entidad, UsuarioErp
from django.contrib.auth.views import LoginView
from django.urls import reverse, reverse_lazy


class SolicitudListView(LoginRequiredMixin, ListView):
    """
    Solo tengo que mostrar el listado de la Entidad a la que pertenece el Usuario Erp
    """
    model = Solicitud
    # paginate_by = 10

    # def get_queryset(self):
    #     return super(SolicitudListView, self).get_queryset().filter(
    #         entidad=self.kwargs['user.usuarioerp.entidad.id']
    #     )
    permission_denied_message = '<strong>Debe iniciar sesión para continuar</strong>    '
    login_url = '/erp/login'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.add_message(request, messages.INFO, self.permission_denied_message)  # added this line
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['aprobadas'] = Solicitud.objects.filter(estado=4).count()
        context['rechazadas'] = Solicitud.objects.filter(estado=3).count()
        context['revision'] = Solicitud.objects.filter(estado=2).count()
        return context



class SolicitudDetailView(LoginRequiredMixin, DetailView):
    model = Solicitud


class SolicitudUpdateView(LoginRequiredMixin, UpdateView):
    model = Solicitud


class EntidadDetailView(LoginRequiredMixin, DetailView):
    model = Entidad
    # template_name = 'solicitudes/entidad_detail.html'


class UsuarioErpDetailView(LoginRequiredMixin, DetailView):
    model = UsuarioErp


class ErpLoginView(LoginView):
    template_name = "solicitudes/registration/login.html"

    def get_success_url(self):
        return reverse_lazy('solicitudes-list')
