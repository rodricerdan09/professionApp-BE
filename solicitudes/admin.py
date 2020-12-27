from django.contrib import admin
from . models import Entidad, UsuarioErp, Solicitud


@admin.register(Entidad)
class AdminEntidad(admin.ModelAdmin):
    list_display = ["id", "nombre", "provincia"]
    list_filter = ["provincia"]

    class Meta:
        model = Entidad


@admin.register(UsuarioErp)
class AdminUsuarioErp(admin.ModelAdmin):
    list_display = ["__str__", "entidad"]
    list_filter = ["entidad"]

    class Meta:
        model = UsuarioErp


@admin.register(Solicitud)
class AdminSolicitud(admin.ModelAdmin):
    list_display = ["__str__", "fecha_alta", "profesional", "estado"]
    list_filter = ["entidad", "estado", "fecha_alta"]
    date_hierarchy = "fecha_alta"
    list_editable = ["estado"]

    class Meta:
        model = Entidad
