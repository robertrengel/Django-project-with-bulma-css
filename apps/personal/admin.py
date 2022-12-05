from django.contrib import admin
from .models import Personal, Skills

# Register your models here.
class PersonaAdmin(admin.ModelAdmin):
    list_display = [
        "first_name",
        "last_name",
        "departamento",
        "job",
        "full_name",
        "id"
    ]
    # Se define una funcion para agregar una columna extra con el dato que retorne la funcion
    def full_name(self, obj):
        return obj.first_name + " " + obj.last_name

    #un buscador para ingresar el nombre y buscalo
    search_fields = ["first_name"]

    # Un filtro que usa los datos que ya existen y filtra a las personas en base a esos
    list_filter = ["departamento","job", "skill"]

    # un firltro horizontal que se usa en las tablas que tiene relaciones de muchos a muchos para
    # mejorar la busqueda de datos al añadir nuevos registros
    filter_horizontal = ["skill"]


admin.site.register(Personal, PersonaAdmin)
admin.site.register(Skills)