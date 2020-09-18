from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


PROVINCIA = [
    (1, "Buenos Aires"),
    (2, "Catamarca"),
    (3, "Chaco"),
    (4, "Chubut"),
    (5, "Córdoba"),
    (6, "Corrientes"),
    (7, "Entre Ríos"),
    (8, "Formosa"),
    (9, "Jujuy"),
    (10, "La Pampa"),
    (11, "La Rioja"),
    (12, "Mendoza"),
    (13, "Misiones"),
    (14, "Neuquén"),
    (15, "Río Negro"),
    (16, "Salta"),
    (17, "San Juan"),
    (18, "San Luis"),
    (19, "Santa Cruz"),
    (20, "Santa Fe"),
    (21, "Santiago del Estero"),
    (22, "Tierra del Fuego, Antártida e Islas del Atlántico Sur"),
    (23, "Tucumán"),

]


class TimeStampedModel(models.Model):
    created = models.DateTimeField(auto_now_add=True, verbose_name='creado',
                                   help_text='fecha de creacion')

    modified = models.DateTimeField(auto_now=True, verbose_name='modificado',
                                    help_text='fecha de modificacion')

    class Meta:
        abstract = True


class Profesion(models.Model):
    name = models.CharField(verbose_name="profesion", max_length=30)
    imagen = models.ImageField("Imagen", upload_to="profesion/", default='profesion/diploma.jpg',
                               null=True, blank=True, max_length=255)
    abbreviation = models.CharField(verbose_name="abreviatura", max_length=10)

    class Meta:
        ordering = ["name"]
        verbose_name = "profesion"
        verbose_name_plural = "profesiones"

    def __str__(self):
        return self.name

    def count_esp(self):
        return Especialidad.objects.filter(profesion=self.pk).count()

    count_esp.empty_value_display = 'S/V'
    count_esp.short_description = "Cant Especialidades"


class Especialidad(models.Model):
    profesion = models.ForeignKey(Profesion, on_delete=models.CASCADE)
    name = models.CharField(verbose_name="especialidad", max_length=30)
    info = models.CharField(verbose_name="detalle", max_length=100, blank=True, null=True)

    class Meta:
        ordering = ["profesion", "name"]
        verbose_name_plural = "especialidades"
        constraints = [
            models.UniqueConstraint(fields=['profesion', "name"], name='profesion - especialidad')
        ]

    def __str__(self):
        return f"{self.profesion}: {self.name}"


class Profesional(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    matricula = models.IntegerField(default=0, blank=True, null=True)
    profesion = models.ForeignKey(Profesion, on_delete=models.DO_NOTHING)
    servicio = models.TextField(blank=True, null=True)
    website_url = models.CharField("Sitio Web", help_text="Ej: www.mipagina.com", max_length=255, blank=True, null=True)
    facebook_url = models.CharField("Facebook",
                                    help_text="Solamente el nombre de su cuenta. Ej: www.facebook.com/micuenta",
                                    max_length=255, blank=True, null=True)
    instagram_url = models.CharField("Instragram",
                                     help_text="Solamente el nombre de su cuenta. Ej: www.instagram.com/micuenta",
                                     max_length=255, blank=True, null=True)

    class Meta:
        ordering = ["usuario__last_name"]
        verbose_name_plural = "Profesionales"

    def __str__(self):
        return f"{self.usuario.last_name},{self.usuario.first_name}"

    def get_absolute_url(self):
        return reverse('home')