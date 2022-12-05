from django.shortcuts import render
from .models import Departamento
from .forms import NewDepartamentoForm
from apps.personal.models import Personal

# Create your views here.
from django.views.generic import TemplateView, ListView, FormView
class PruebaInicio(TemplateView):
    template_name = "departamento/inicio.html"

class IndexView(TemplateView):
    template_name = "index.html"


class DepaLista(ListView):
    model = Departamento
    context_object_name = "lista"
    template_name = "departamento/lista.html"

class NewDepartamentoView(FormView):
    template_name = "departamento/new_departamento.html"
    form_class = NewDepartamentoForm
    success_url = "/"

    def form_valid(self, form):
        # primer metodo para agregar registros a la base de datos usando el .save()
         
        #depa = Departamento(
        #    name = form.cleaned_data["departamento"],
        #    short_name = form.cleaned_data["shortname"]
        #)
        #depa.save()


        # segundo metodo para agregar registros a la base de datos usando el cleaned_data
        departamento = form.cleaned_data["departamento"]
        shortname = form.cleaned_data["shortname"]
        first_name = form.cleaned_data["first_name"]
        last_name = form.cleaned_data["last_name"]
    
        depa = Departamento.objects.create(
            name = departamento,
            short_name = shortname,

        )
        Personal.objects.create(
            first_name=first_name,
            last_name=last_name,
            job = "1",
            departamento = depa

        )
        return super(NewDepartamentoView, self).form_valid(form)


class Personal_departamento_ListView(ListView):
    template_name = "departamento/personal_departamento.html"
    context_object_name = "personal"
    model = Personal

    def get_queryset(self):
        area = self.kwargs["departamento"]
        lista = Personal.objects.filter(
            departamento= area.lower()
        )
        return lista 


