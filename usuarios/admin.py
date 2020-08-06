from django.contrib import admin
from .models import Usuario, UsuarioErp, Profesional


@admin.register(UsuarioErp)
class AdminUsuarioErp(admin.ModelAdmin):
    list_display = ['nombre', 'email', 'entidad']  # es lo que se muestra en la grilla
    list_filter = ['entidad']
    search_fields = ['nombre']

    class Meta:
        model = UsuarioErp


@admin.register(Profesional)
class AdminProfesional(admin.ModelAdmin):
    list_display = ['apellido', 'profesion', 'especialidad']
    list_filter = ['profesion']  # filtro a la derecha

    fieldsets = (
            (
                "Datos Personales", {
                    'fields': (
                        ('apellido', 'nombre'), "email"
                    )
                }
            ),

            ("Informacion Profesional", {
                'fields': ("matricula", "profesion", "especialidad"
                           ),
            }
             ),
    )

    class Meta:
        model = Profesional


@admin.register(Usuario)
class AdminUsuario(admin.ModelAdmin):
    list_display = ['nombre', 'email']  # es lo que se muestra en la grilla
    search_fields = ['nombre']

    class Meta:
        model = Usuario


admin.site.site_header = "ProfessionalApp | Administrador"
admin.site.index_title = "ProfessionalApp | Admin Dashboard"
