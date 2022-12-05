from random import choices
from django.db import models

from apps.departamento.models import Departamento

class Skills(models.Model):
    skill = models.CharField("Habilidades", max_length=50)

    class Meta:
        verbose_name = "Habilidad"
        verbose_name_plural = "Habilidades"

    def __str__(self):
        return self.skill 


# Create your models here.
class Personal(models.Model):
    JOB_CHOICES = (
        ("0", "Structural Engineer"),
        ("1", "Associate Professor"),
        ("2", "Financial Analyst"),
        ("3", "Marketing Manager"),
        ("4", "Help Desk Operator"),
        ("5", "Account Coordinator"),
        ("6", "Web Designer III"),
        ("7", "Registered Nurse"),
        ("8", "Librarian"),
        ("9", "Junior Executive"),
        
    )
    first_name = models.CharField("Nombre",max_length = 50)
    last_name = models.CharField("Apellido",max_length = 50)
    full_name = models.CharField("Nombre completo",max_length = 120, blank = True)
    job = models.CharField("Trabajo",max_length = 2, choices  = JOB_CHOICES)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    skill = models.ManyToManyField(Skills)
    image = models.ImageField(upload_to="empleado", height_field=None, width_field=None, max_length=None, blank=True, null=True)

    def __str__(self):
        return self.skill