from django.db import models
from django.contrib.auth.models import User
from accounts.models import Profesional


class Entidad(models.Model):
    CHACO = 1
    CORRIENTES = 2
    FORMOSA = 3
    MISIONES = 4

    PROV_CHOICES = [
        (CHACO, "Chaco"),
        (CORRIENTES, "Corrientes"),
        (FORMOSA, "Formosa"),
        (MISIONES, "Misiones"),
    ]

    nombre = models.CharField(verbose_name="Nombre de la entidad", max_length=50)
    provincia = models.PositiveSmallIntegerField(blank=False,
                                                 null=True,
                                                 choices=PROV_CHOICES,
                                                 default=1
                                                 )

    class Meta:
        verbose_name = "entidad"
        verbose_name_plural = "entidades"

    def __str__(self):
        return f"{self.nombre.title()} - ({self.get_provincia_display()})"


class UsuarioErp(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    entidad = models.ForeignKey(Entidad, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "usuario Erp"
        verbose_name_plural = "usuarios Erp"

    def __str__(self):
        if len(self.usuario.last_name) > 0:
            return f"{self.usuario.last_name.title()},{self.usuario.first_name.title()} - ({self.entidad.nombre.title()})"
        else:
            return f"@{self.usuario.username}"


class Solicitud(models.Model):

    INICIADO = 1
    EN_REVISION = 2
    ANULADA = 3
    APROBADA = 4

    ESTADO_CHOICES = [
        (INICIADO, "Iniciado"),
        (EN_REVISION, "En Revision"),
        (ANULADA, "Anulada"),
        (APROBADA, "Aprobada"),
    ]

    profesional = models.ForeignKey(Profesional, on_delete=models.DO_NOTHING)
    entidad = models.ForeignKey(Entidad, on_delete=models.DO_NOTHING,
                                blank=False,
                                null=False)
    fecha_alta = models.DateTimeField(auto_now_add=True, verbose_name='creado', help_text='fecha de creacion')
    aprobado_por = models.ForeignKey(UsuarioErp, verbose_name='aprobado por', on_delete=models.DO_NOTHING,
                                     blank=True,
                                     null=True)
    fecha_aprobacion = models.DateTimeField(help_text='fecha de aprobacion',
                                            null=True,
                                            blank=True)
    observacion = models.CharField(help_text="Aqui puede agregar una observacion",
                                   max_length=50,
                                   default="",
                                   blank=True,
                                   null=True)
    estado = models.PositiveSmallIntegerField(blank=False,
                                              null=False,
                                              choices=ESTADO_CHOICES,
                                              default=1
                                              )

    class Meta:
        verbose_name = "solicitud"
        verbose_name_plural = "solicitudes"

    def __str__(self):
        return f"Solicitud nro: {self.id}"
