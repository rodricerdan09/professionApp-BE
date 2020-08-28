# from django.shortcuts import render, get_list_or_404
from django.contrib import messages
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from .models import Profesion, Especialidad
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin


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
            messages.error(request, 'Su cuenta ha sido eliminada')
            return super(UserDeleteView, self).post(request, *args, **kwargs)


class UserDesactivarCuentaView(LoginRequiredMixin, UpdateView):
    model = User
    fields = ('last_name', 'first_name', 'email')
    template_name = 'accounts/user_update.html'
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
