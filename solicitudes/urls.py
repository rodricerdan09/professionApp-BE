import django.contrib.auth.urls
from django.urls import path, include
from .views import SolicitudListView, SolicitudDetailView
from .views import EntidadDetailView
from .views import UsuarioErpDetailView

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('solicitudes/', SolicitudListView.as_view(), name='solicitudes-list'),
    path('solicitud/<int:pk>', SolicitudDetailView.as_view(), name='solicitud-detail'),
    path('entidad/<int:pk>', EntidadDetailView.as_view(), name='entidad-detail'),
    path('cuenta/<int:pk>', UsuarioErpDetailView.as_view(), name='usuarioerp-detail'),
]

