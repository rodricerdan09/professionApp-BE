# from django.shortcuts import render, get_list_or_404
from django.contrib import messages
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from .models import Profesion, Especialidad, Profesional
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import ProfileCreationForm


class ProfesionListView(ListView):
    model = Profesion
    paginate_by = 10


class EspecialidadListView(ListView):
    model = Especialidad
    template_name = 'accounts/especialidad_list.html'

    def get_queryset(self):
        return super(EspecialidadListView, self).get_queryset().filter(
            profesion__name=self.kwargs['profesion_nombre']
        )


class ProfesionalporProfesionListView(ListView):
    model = Profesional
    paginate_by = 8
    template_name = 'accounts/profesional_por_profesion_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total'] = Profesional.objects.filter(profesion=self.kwargs['pk']).count()
        return context

    def get_queryset(self):
        return super(ProfesionalporProfesionListView, self).get_queryset().filter(
            profesion=self.kwargs['pk']
        )


class ProfesionalListView(ListView):
    model = Profesional
    paginate_by = 8

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total'] = Profesional.objects.count()
        return context


class UserDetailView(LoginRequiredMixin, DetailView):
    model = User

    slug_field = 'username'
    slug_url_kwarg = 'username'

    # queryset = User.objects.get()
    template_name = 'accounts/user_detail.html'
    # TODO: mirar si reemplazar para nuevos usuarios
    # def get_object(self):
    #     id_ = self.kwargs.get("pk")
    #     print(id_)
    #     return get_list_or_404(User, id=id_)


class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    fields = ('last_name', 'first_name', 'email')
    template_name = 'accounts/user_update.html'

    # def get_absolute_url(self):
    #     return reverse("user-detail", kwargs={"id": self.id})
    #
    def get_absolute_url(self):
        return reverse('user-detail', args=[str(self.id)])


class UserDeleteView(LoginRequiredMixin, DeleteView):
    model = User
    template_name = 'accounts/user_confirm_delete.html'
    success_url = reverse_lazy('home')

    def post(self, request, *args, **kwargs):
        if "cancel" in request.POST:
            url = self.success_url
            return HttpResponseRedirect(url)
        else:
            user = request.user
            nombre = user.get_username()
            messages.error(request, f'@{nombre} eliminaste tu cuenta. Te vamos a extrañar :(')
            return super(UserDeleteView, self).post(request, *args, **kwargs)


class UserDesactivarCuentaView(LoginRequiredMixin, UpdateView):
    model = User
    fields = ('is_active',)
    template_name = 'accounts/user_desactivar.html'
    success_url = reverse_lazy('home')

    def post(self, request, *args, **kwargs):
        url = self.success_url
        if "cancel" in request.POST:
            return HttpResponseRedirect(url)
        else:
            user = request.user
            user.is_active = False
            user.save()
            nombre = user.get_username()
            mensaje = f'@{nombre}, tu cuenta ha sido desactivada.\n ' \
                      f'Para activarla nuevamente comunicarse con info@professionap.com'
            logout(request)
            messages.warning(request, mensaje)
            return HttpResponseRedirect(url)


class CrearPerfilProfesional(CreateView):
    model = Profesional
    form_class = ProfileCreationForm
    template_name = 'registration/crear_perfil.html'

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)


class ProfesionalDetailView(LoginRequiredMixin, DetailView):
    model = Profesional
    template_name = 'accounts/profesional_detail_nuevo.html'
    permission_denied_message = '<strong>Debe iniciar sesión para continuar</strong>    '
    login_url = '/cuenta/login'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.add_message(request, messages.INFO, self.permission_denied_message)  # added this line
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)


class ProfesionalUpdateView(LoginRequiredMixin, UpdateView):
    model = Profesional
    fields = ('profesion', 'matricula', 'telefono', 'website_url', 'facebook_url', 'instagram_url', 'servicio')
    template_name = 'accounts/profesional_update.html'

    def get_absolute_url(self):
        return reverse_lazy('profesional-detail', self.id)


class ProfesionalUpdateNuevoView(LoginRequiredMixin, UpdateView):
    model = Profesional
    fields = ('profesion', 'matricula', 'telefono', 'profile_pic', 'website_url', 'facebook_url', 'instagram_url', 'servicio')
    template_name = 'accounts/profesional_update_nuevo.html'

    def get_absolute_url(self):
        return reverse_lazy('profesional-detail', self.id)