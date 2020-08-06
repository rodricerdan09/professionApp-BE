from django.urls import path
from .apiviews import ProfesionList, ProfesionDetail, ProfesionEspecialidadDetail
from .apiviews import EspecialidadList, EspecialidadDetail

app_name = 'profesionales'

urlpatterns = [
    path('profesiones/', ProfesionList.as_view(), name='profesion_list'),
    path('profesiones/<int:pk>/', ProfesionDetail.as_view(), name='profesion_detail'),
    path('profesiones/<int:pk>/especialidades/', EspecialidadList.as_view(), name='especialidad_list'),
    path('profesiones/<int:profesion_pk>/especialidades/<int:pk>', ProfesionEspecialidadDetail.as_view(), name='especialidad_detail'),
    path('especialidades/<int:pk>', EspecialidadDetail.as_view(), name='especialidad_detail'),
]
