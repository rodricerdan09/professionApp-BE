from django.contrib import admin
from django.urls import path, include, re_path
from django.views.static import serve
from django.conf import settings
from accounts.views import ProfesionListView, EspecialidadListView
from .views import HomePageView, SignUpView


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('admin/', admin.site.urls),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('cuenta/', include('accounts.urls')),
    path('profesiones/', ProfesionListView.as_view(), name='profesion-list'),
    path('profesiones/<str:profesion_nombre>/', EspecialidadListView.as_view(), name='especialidad-list'),
]

urlpatterns += [
    re_path(r'^media/(?P<path>.*)$', serve, {
        'document_root': settings.MEDIA_ROOT,
    })
]

handler404 = 'src.views.error_404_view'
