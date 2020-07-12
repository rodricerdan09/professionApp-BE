from django.db import models

PROVINCIA = [
    (1, "Chaco"),
    (2, "Corrientes"),
    (3, "Formosa"),
    (4, "Misiones"),
]

# TODO buscar el nombre de las entidades de chaco corrientes formosa
# TODO armar json para carga de entidades


class Entidad(models.Model):
    nombre = models.CharField(max_length=50)
    provincia = models.PositiveSmallIntegerField(blank=False,
                                                 null=True,
                                                 choices=PROVINCIA,
                                                 default=1
                                                 )

    def __str__(self):
        return f"{self.nombre} - ({self.get_provincia_display()})"

    class Meta:
        verbose_name = "entidad"
        verbose_name_plural = "entidades"


class Solicitud(models.Model):
    entidad = models.ForeignKey(Entidad, on_delete=models.DO_NOTHING)
    profesional = models.ForeignKey('usuarios.Profesional', on_delete=models.DO_NOTHING)
    autorizado = models.BooleanField(default=False)
    autorizado_por = models.ForeignKey('usuarios.UsuarioErp',
                                       blank=True, null=True,
                                       on_delete=models.DO_NOTHING)
    autorizado_fecha = models.DateTimeField()

    def __str__(self):
        return f"Solitud nro: {self.id}"

    class Meta:
        verbose_name = "solicitud"
        verbose_name_plural = "solicitudes"
