from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView
from django.urls import reverse_lazy
from accounts.forms import UserCreationForm
from django.contrib.messages.views import SuccessMessageMixin
from accounts.models import Profesion, Profesional
from accounts.filters import ProfesionalFilter
from django.db.models import Q


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


class BuscarResultView(ListView):
    model = Profesional
    paginate_by = 6
    template_name = 'resultados_profesional.html'
    myFilter = ProfesionalFilter()

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Profesional.objects.filter(
            Q(profesion__name__icontains=query) | Q(servicio__icontains=query)
        )
        return object_list

    def get_context_data(self, **kwargs):
        qs = self.request.GET.get('q')
        context = super().get_context_data(**kwargs)
        context['total'] = Profesional.objects.filter(
            Q(profesion__name__icontains=qs) | Q(servicio__icontains=qs)
        ).count()
        context['query'] = qs
        context['filter'] = ProfesionalFilter(self.request.GET, queryset=self.get_queryset())
        return context
