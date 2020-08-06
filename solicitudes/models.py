from django.db import models

# TODO buscar el nombre de las entidades de chaco corrientes formosa
# TODO armar json para carga de entidades


class Entidad(models.Model):
    CHACO = 1
    CORRIENTES = 2
    FORMOSA = 3
    MISIONES = 4

    PROVINCIA_CHOICES = [
        (CHACO, "Chaco"),
        (CORRIENTES, "Corrientes"),
        (FORMOSA, "Formosa"),
        (MISIONES, "Misiones"),
    ]

    nombre = models.CharField(max_length=50)
    provincia = models.PositiveSmallIntegerField(blank=False,
                                                 null=True,
                                                 choices=PROVINCIA_CHOICES,
                                                 default=1
                                                 )

    def __str__(self):
        return f"{self.nombre} - ({self.get_provincia_display()})"

    class Meta:
        verbose_name = "entidad"
        verbose_name_plural = "entidades"


# class Solicitud(models.Model):
#     entidad = models.ForeignKey(Entidad, on_delete=models.DO_NOTHING)
#     profesional = models.ForeignKey('usuarios.Profesional', on_delete=models.DO_NOTHING)
#     autorizado = models.BooleanField(default=False)
#     autorizado_por = models.ForeignKey('usuarios.UsuarioErp',
#                                        blank=True, null=True,
#                                        on_delete=models.DO_NOTHING)
#     autorizado_fecha = models.DateTimeField(blank=True, null=True)
#
#     def __str__(self):
#         return f"Solitud nro: {self.id}"
#
#     class Meta:
#         verbose_name = "solicitud"
#         verbose_name_plural = "solicitudes"
