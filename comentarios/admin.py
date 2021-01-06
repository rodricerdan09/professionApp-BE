from django.contrib import admin
from .models import Comentario


@admin.register(Comentario)
class AdminComentario(admin.ModelAdmin):
    list_display = ["resumen", "profesional", "creador", "created", "modified"]
