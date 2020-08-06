from django.db import models


class Usuario(models.Model):
    nombre = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return self.email


class Profesional(Usuario):
    apellido = models.CharField(max_length=20)
    matricula = models.IntegerField(blank=True, null=True)
    profesion = models.ForeignKey(
        'profesionales.Profesion',
        related_name='profesional_profesion',
        blank=False,
        null=False,
        on_delete=models.DO_NOTHING)
    especialidad = models.ForeignKey(
        'profesionales.Especialidad',
        related_name='profesional_especialidad',
        blank=False,
        null=False,
        on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"{self.apellido}. {self.profesion} ({self.especialidad})"

    class Meta:
        verbose_name = 'profesional'
        verbose_name_plural = 'profesionales'


class UsuarioErp(Usuario):
    entidad = models.ForeignKey(
        'solicitudes.Entidad',
        related_name='usuarioErp_entidad',
        on_delete=models.DO_NOTHING)
    # antes de migrar la primera vez

    def __str__(self):
        return f"{self.nombre} (erp) | {self.entidad}"

    class Meta:
        verbose_name = 'usuario Erp'
        verbose_name_plural = 'usuarios Erp'


# TODO definir el tema de los permisos, que grupos voy a tener ?
# TODO cambiar el nombre de las tablas usando "db_table = 'nombresingular'"
# TODO el profesional se relacion con profesion y especialidad o solo especialidad ?
