from django.db import models
from django.contrib.auth.models import User
from accounts.models import Profesional
from .utils import CreationModificationDateMixin


class Comentario(CreationModificationDateMixin):
    profesional = models.ForeignKey(Profesional,
                                    related_name="comentarios",
                                    on_delete=models.CASCADE)
    creador = models.ForeignKey(User, on_delete=models.CASCADE)
    mensaje = models.TextField()

    class Meta:
        ordering = ["-modified"]
        constraints = [
            models.UniqueConstraint(
                fields=['creador', "profesional"],
                name='comentario - profesional'
            )
        ]

    def __str__(self):
        return f"Para {self.profesional}, de {self.creador.username}."

    def resumen(self):
        return f"{self.mensaje[:25]}"
