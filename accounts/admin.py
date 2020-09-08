from django.contrib import admin
from .models import Profesion, Especialidad, Profesional


class InLineEspecialidad(admin.StackedInline):
    """
    Agrego en la Profesion como maximo 3 niveles para agregar Especialidades
    """
    model = Especialidad
    # extra = 2
    max_num = 3


@admin.register(Profesion)
class AdminProfesion(admin.ModelAdmin):
    inlines = [InLineEspecialidad]
    list_display = ['name', 'abbreviation', 'count_esp']  # es lo que se muestra en la grilla

    class Meta:
        model = Profesion


@admin.register(Especialidad)
class AdminEspecialidad(admin.ModelAdmin):
    list_display = ['name', 'profesion']  # es lo que se muestra en la grilla
    list_filter = ['profesion']  # filtro a la derecha
    search_fields = ['profesion__nombre', "name"]  # se agrega un buscador encima
    #  busco por nombre de especialidad o por nombre de la profesion

    class Meta:
        model = Especialidad


@admin.register(Profesional)
class AdminEspecialidad(admin.ModelAdmin):
    list_display = ['__str__', 'profesion', 'matricula']  # es lo que se muestra en la grilla
    list_filter = ['profesion']  # filtro a la derecha

    class Meta:
        model = Profesional


admin.site.site_header = "ProfessionalApp | Administrador"
admin.site.index_title = "ProfessionalApp | Admin Dashboard"
