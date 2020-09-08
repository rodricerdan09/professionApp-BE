from django.urls import path, include
from .views import UserDetailView, UserUpdateView, UserDeleteView, UserDesactivarCuentaView
from django.contrib.auth import urls
from .views import CrearPerfilProfesional, ProfesionalDetailView, ProfesionalUpdateView

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('misdatos/<slug:username>', UserDetailView.as_view(), name='user-detail'),
    path('misdatos/actualizar/<int:pk>', UserUpdateView.as_view(), name='user-update'),
    path('misdatos/profesional/<int:pk>', ProfesionalDetailView.as_view(), name='profesional-detail'),
    path('misdatos/borrar/<int:pk>', UserDeleteView.as_view(), name='user-delete'),
    path('misdatos/desactivar/<int:pk>', UserDesactivarCuentaView.as_view(), name='desactivar'),
    path('misdatos/profesional/nuevo', CrearPerfilProfesional.as_view(), name='crear-perfil'),
    path('misdatos/profesional/actualizar/<int:pk>', ProfesionalUpdateView.as_view(), name='profesional-update')

]
