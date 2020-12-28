from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, UpdateView, CreateView
from .models import Solicitud, Entidad, UsuarioErp
from django.contrib.auth.views import LoginView
from django.urls import reverse, reverse_lazy
from .forms import SolicitudCreationForm
import datetime


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
        context['nuevas'] = Solicitud.objects.filter(estado=1, entidad=self.request.user.usuarioerp.entidad).count()
        context['revision'] = Solicitud.objects.filter(estado=2, entidad=self.request.user.usuarioerp.entidad).count()
        context['rechazadas'] = Solicitud.objects.filter(estado=3, entidad=self.request.user.usuarioerp.entidad).count()
        context['aprobadas'] = Solicitud.objects.filter(estado=4, entidad=self.request.user.usuarioerp.entidad).count()
        return context

    def get_queryset(self):
        return super(SolicitudListView, self).get_queryset().filter(
            entidad=self.request.user.usuarioerp.entidad
        )


class SolicitudDetailView(LoginRequiredMixin, DetailView):
    model = Solicitud


class SolicitudUpdateView(LoginRequiredMixin, UpdateView):
    model = Solicitud
    fields = ('estado', 'observacion')

    def get_success_url(self):
        return reverse_lazy('solicitudes-list')


class SolicitudCreateView(LoginRequiredMixin, CreateView):
    model = Solicitud
    form_class = SolicitudCreationForm
    template_name = 'solicitudes/solicitud_nueva.html'
    # template_name = 'registration/crear_perfil.html'

    def form_valid(self, form):
        form.instance.profesional = self.request.user.profesional
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = datetime.datetime.now()
        return context


class EntidadDetailView(LoginRequiredMixin, DetailView):
    model = Entidad
    # template_name = 'solicitudes/entidad_detail.html'


class UsuarioErpDetailView(LoginRequiredMixin, DetailView):
    model = UsuarioErp


class ErpLoginView(LoginView):
    template_name = "solicitudes/registration/login.html"

    def get_success_url(self):
        return reverse_lazy('solicitudes-list')

