from django.db import models


class Profesion(models.Model):
    nombre = models.CharField(max_length=20)
    nombre_corto = models.CharField(max_length=5)
    entidad = models.ManyToManyField(
        'solicitudes.Entidad',
        related_name='profesion_entidad',
        blank=True)  # antes de migrar la primera vez

    def __str__(self):
        return self.nombre

    def count_esp(self):
        return Especialidad.objects.filter(profesion=self.pk).count()

    count_esp.empty_value_display = 'S/V'
    count_esp.short_description = "Cant Especialidades"

    class Meta:
        verbose_name = 'profesion'
        verbose_name_plural = 'profesiones'


class Especialidad(models.Model):
    nombre = models.CharField(max_length=20)
    profesion = models.ForeignKey(
        Profesion,
        related_name='especialidad_profesion',
        on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre}"

    class Meta:
        verbose_name = 'especialidad'
        verbose_name_plural = 'especialidades'
