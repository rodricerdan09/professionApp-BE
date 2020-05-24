# from django.shortcuts import render, get_list_or_404
from django.views.generic import ListView, DetailView
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
    # queryset = User.objects.get()
    template_name = 'accounts/user_detail.html'
    # TODO: mirar si reemplazar para nuevos usuarios
    # def get_object(self):
    #     id_ = self.kwargs.get("pk")
    #     print(id_)
    #     return get_list_or_404(User, id=id_)
