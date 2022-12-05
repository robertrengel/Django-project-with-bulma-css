from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Departamento(models.Model):
    name = models.CharField("Nombre",max_length = 50)
    short_name = models.CharField("nombre Corto",max_length = 50)
    anulate = models.BooleanField("anulado", default = False)

    class Meta:
        verbose_name = "Departamento"
        verbose_name_plural = "Departamento"
        ordering = ["name"]
        unique_together = ("name", "short_name")

    def __str__(self):
        return self.name