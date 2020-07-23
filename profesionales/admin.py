from django.contrib import admin
from .models import Especialidad, Profesion


@admin.register(Profesion)
class AdminProfesion(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'count_esp', 'count_entidad']  # es lo que se muestra en la grilla
    ordering = ('nombre',)

    def count_entidad(self, obj):
        return obj.entidad.all().count()

    count_entidad.empty_value_display = 'S/V'
    count_entidad.short_description = "Cant de Entidad/Colegio"

    class Meta:
        model = Profesion


@admin.register(Especialidad)
class AdminEspecialidad(admin.ModelAdmin):
    list_display = ['nombre', 'profesion']  # es lo que se muestra en la grilla
    list_filter = ['profesion']  # filtro a la derecha
    search_fields = ['profesion__nombre', "nombre"]  # se agrega un buscador encima
    #  busco por nombre de especialidad o por nombre de la profesion

    class Meta:
        model = Especialidad


