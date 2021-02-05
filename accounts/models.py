from datetime import time
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from comentarios.models import Comentario

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
        return self.name.title()

    def count_esp(self):
        return Especialidad.objects.filter(profesion=self.pk).count()

    count_esp.empty_value_display = 'S/V'
    count_esp.short_description = "Cant Especialidades"

    def count_profesionales(self):
        return Profesional.objects.filter(profesion=self.pk).count()

    count_profesionales.empty_value_display = 'S/V'
    count_profesionales.short_description = "Cant Profesionales"


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


class Horario(models.Model):
    DIAS = [
        (1, "Lunes a Viernes"),
        (2, "Lunes a Sábado"),
        (3, "Lunes"),
        (4, "Martes"),
        (5, "Miercoles"),
        (6, "Jueves"),
        (7, "Viernes"),
        (8, "Sábado"),
        (9, "Domingo"),
    ]

    DEFAULT_HORA_INICIO = time(hour=8)
    DEFAULT_HORA_FIN = time(hour=16)

    weekday = models.IntegerField("Dia", choices=DIAS, default=1)
    from_hour = models.TimeField("Hora desde", default=DEFAULT_HORA_INICIO)
    to_hour = models.TimeField("Hora hasta", default=DEFAULT_HORA_FIN)

    class Meta:
        ordering = ('weekday', 'from_hour', 'to_hour')
        unique_together = ('weekday', 'from_hour', 'to_hour')

    def __str__(self):
        inicio = self.from_hour.strftime('%H:%M')
        fin = self.to_hour.strftime('%H:%M')
        return f"{self.get_weekday_display()} de {inicio} hs a {fin} hs"


class Direccion(models.Model):
    CIUDAD = [
        (3, "Barranqueras"),
        (2, "Corrientes"),
        (1, "Resistencia"),
    ]

    LUGAR_TRABAJO = [
        (1, "Oficina"),
        (2, "Consultorio"),
        (4, "Empresa"),
        (3, "Domicilio particular"),
    ]

    calle = models.CharField(max_length=100, blank=False, null=False)
    numero = models.PositiveSmallIntegerField()
    ciudad = models.PositiveSmallIntegerField(choices=CIUDAD, default=1)
    piso_dpto = models.CharField("Piso/Dpto", help_text="Opcional",
                                 max_length=5, blank=True, null=True)
    lugar = models.PositiveSmallIntegerField("Lugar de trabajo", choices=LUGAR_TRABAJO, default=1)

    class Meta:
        ordering = ["calle"]
        verbose_name_plural = "Direcciones"

    def __str__(self):
        return f"{self.calle.title()} {self.numero} ({self.get_ciudad_display()})"


class Profesional(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    matricula = models.IntegerField(default=0, blank=True, null=True)
    profesion = models.ForeignKey(Profesion, on_delete=models.DO_NOTHING)
    servicio = models.TextField(blank=True, null=True)
    telefono = models.PositiveIntegerField(help_text="Ingrese solo numeros", null=True, blank=True)
    profile_pic = models.ImageField("Avatar", upload_to="", default="avatar7.png", null=True, blank=False,
                                    max_length=255)
    website_url = models.CharField("Sitio Web", help_text="Ej: www.mipagina.com", max_length=255, blank=True, null=True)
    facebook_url = models.CharField("Facebook",
                                    help_text="Solamente el nombre de su cuenta. Ej: www.facebook.com/micuenta",
                                    max_length=255, blank=True, null=True)
    instagram_url = models.CharField("Instragram",
                                     help_text="Solamente el nombre de su cuenta. Ej: www.instagram.com/micuenta",
                                     max_length=255, blank=True, null=True)
    horarios = models.ManyToManyField(Horario,
                                      help_text="Mantenga presionada la tecla 'Ctrl' para seleccionar mas de uno"
                                      )
    direccion = models.ForeignKey(Direccion, on_delete=models.CASCADE, blank=False, null=True)
    favoritos = models.ManyToManyField(User, related_name='prof_favoritos')

    class Meta:
        ordering = ["usuario__last_name"]
        verbose_name_plural = "Profesionales"

    def __str__(self):
        return f"{self.profesion.abbreviation.title()}: {self.usuario.last_name.title()},{self.usuario.first_name.title()}"

    def get_absolute_url(self):
        return reverse('home')

    def admin_horarios(self):
        return ' | '.join([str(h) for h in self.horarios.all()])

    admin_horarios.short_description = "Horarios"

    @property
    def num_de_comentarios(self):
        return Comentario.objects.filter(profesional=self.id).count()