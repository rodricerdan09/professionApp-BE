from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from django.urls import reverse_lazy
from accounts.forms import UserCreationForm
from django.contrib.messages.views import SuccessMessageMixin
from accounts.models import Profesion


class HomePageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profesiones'] = Profesion.objects.all()
        return context


class SignUpView(SuccessMessageMixin, CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')
    success_message = '<strong>Bienvenido!</strong> Cuenta creada! Ya a puedes iniciar sesion'


def error_404_view(request, exception):
    return render(request, '404.html')
    # TODO: poner en modo debug = False
