from django.shortcuts import render
from .models import Personal
from django.urls import reverse_lazy
from .forms import PersonalForm
from django.db.models import Q


# Create your views here.
from django.views.generic import TemplateView, ListView, CreateView, DetailView, UpdateView, DeleteView

class InicioPersonal(TemplateView):
    template_name = "personal/inicio.html"

class InicioListaDatos(ListView):
    """Listar todos los empleados"""
    model = Personal
    paginate_by = 4
    template_name = "personal/listaDatos.html"

    def get_queryset(self):
        keyword = self.request.GET.get("kword","")

        # este metodo de filtrado usa la | para filtrar pero hay que escribi mas codigo.
        lista = Personal.objects.filter(first_name__icontains = keyword.lower()
        ) | Personal.objects.filter(last_name__icontains = keyword.lower())

        #NOTA si se quiere hacer un filtado con AND se escribe de esta manera, la coma actua como AND
        #lista = Personal.objects.filter(first_name__icontains = keyword.lower(),last_name__icontains = keyword.lower())

        #este metodo de filtrado usa una libreria Q que esta arriba pero  no  se esta usando.
        # lista = Personal.objects.filter(
        #     Q(first_name__icontains = keyword.lower()) |
        #     Q(last_name__icontains = keyword.lower())
        # )
        return lista

class ListByAreaEmployee(ListView):
    """Listar los empleados por area usando un filtrado poco practico"""

    #template_name = "personal/list_employee_by_area.html"
    #queryset = Personal.objects.filter(
    #    departamento__name = "programacion"
    #)

    #---------------------------------------------------------------------------
    """Listar los empleados por area usando filtrado recogiendo
    el area de trabajo desde la url"""

    template_name = "personal/list_employee_by_area.html"
    context_object_name = "personal"
    def get_queryset(self):
        area = self.kwargs["name"]
        lista = Personal.objects.filter(
            departamento__name = area
        )
        return lista 
    #----------------------------------------------------------------------------

class ListEmployeeByKeyword(ListView):
    """Lista de empleados usando una palabra clave"""
    template_name = "personal/lista_empleados_keyword.html"
    context_object_name = "empleados"

    def get_queryset(self):
        keyword = self.request.GET.get("kword","")
        lista = Personal.objects.filter(
            first_name = keyword.lower()
        )
        return lista

class ListSkillsEmployee(ListView):
    template_name = "personal/lista_skills.html"
    context_object_name = "skills"

    def get_queryset(self):
        personal = Personal.objects.get(id = 9)
        return personal.skill.all()

#----Esta clase es una calse de prueba para probar las createviews
class CrearDatoPersonal(CreateView):
    model = Personal
    template_name = "personal/crear_datos_personal.html"
    fields = ['first_name']
#----------------------------------------------------------------

class DetallePersonal(DetailView):
    model = Personal
    template_name = "personal/detalle_personal.html"


class SuccesPersonal(TemplateView):
    template_name = "personal/succes.html"

class DeletePersonal(TemplateView):
    template_name = "personal/delete.html"

class Add_Personal(TemplateView):
    template_name = "personal/success_new_person.html"



class SumarPersonal(CreateView):
    model = Personal
    template_name = "personal/add_personal.html"
    form_class = PersonalForm
    success_url = reverse_lazy("personal_app:new_personal")

    def form_valid(self, form):
        #logica del proceso
        personal = form.save(commit= False)
        personal .full_name = personal.first_name + " " + personal.last_name
        personal.save()
        return super(SumarPersonal, self).form_valid(form)



class PersonalUpdateView(UpdateView):
    template_name = "personal/update_personal.html"
    model = Personal
    form_class = PersonalForm
    success_url = reverse_lazy("personal_app:succes")


class PersonalDeleteView(DeleteView):
    model = Personal
    template_name = "personal/delete_personal.html"
    success_url = reverse_lazy("personal_app:delete")
    context_object_name = "empleados"

class AdminListaDatos(ListView):
    """Listar todos los empleados"""
    model = Personal
    paginate_by = 8
    template_name = "personal/admin_personal.html"


