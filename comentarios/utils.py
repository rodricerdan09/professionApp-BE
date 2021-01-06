from django.db import models


class CreationModificationDateMixin(models.Model):
    """
    Clase abstracta base con fecha de creacion y modificacion
    """
    created = models.DateTimeField(auto_now_add=True, verbose_name='creado',
                                   help_text='fecha de creacion')

    modified = models.DateTimeField(auto_now=True, verbose_name='modificado',
                                    help_text='fecha de modificacion')

    class Meta:
        abstract = True

    def creado(self):
        return f"Creado: {self.created}"

    def modificado(self):
        return f"Modificado: {self.modified}"
