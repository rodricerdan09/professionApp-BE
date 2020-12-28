import django.contrib.auth.urls
from django.urls import path, include
from .views import SolicitudListView, SolicitudDetailView, SolicitudCreateView, SolicitudUpdateView
from .views import EntidadDetailView
from .views import UsuarioErpDetailView
from .views import ErpLoginView

urlpatterns = [
    path('login/', ErpLoginView.as_view(), name='login-erp'),
    # path('password_change/', ErpPasswordChange.as_view(), name='password-erp'),

    path('solicitudes/', SolicitudListView.as_view(), name='solicitudes-list'),
    path('solicitud/<int:pk>', SolicitudDetailView.as_view(), name='solicitud-detail'),
    path('solicitud/editar/<int:pk>', SolicitudUpdateView.as_view(), name='solicitud-update'),
    path('solicitud/nueva', SolicitudCreateView.as_view(), name='solicitud-create'),
    path('entidad/<int:pk>', EntidadDetailView.as_view(), name='entidad-detail'),
    path('cuenta/<int:pk>', UsuarioErpDetailView.as_view(), name='usuarioerp-detail'),
]

