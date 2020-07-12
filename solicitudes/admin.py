from django.contrib import admin
from .models import Entidad
# Solicitud


@admin.register(Entidad)
class AdminEntidad(admin.ModelAdmin):
    list_display = ['nombre', 'provincia']  # es lo que se muestra en la grilla
    list_filter = ['provincia']  # filtro de la derecha
    search_fields = ['nombre']  # barra de busqueda

    class Meta:
        model = Entidad


# @admin.register(Solicitud)
# class AdminSolicitud(admin.ModelAdmin):
#     list_display = ['__str__', 'profesional', 'entidad']
#     list_filter = ['entidad']
#     fields = ['profesional', 'entidad']
#
#     class Meta:
#         model = Solicitud
