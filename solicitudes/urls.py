from django.urls import path
from .views import entidad_detail, entidad_list

urlpatterns = [
    path('entidades/', entidad_list),
    path('entidades/<int:pk>', entidad_detail),
]


