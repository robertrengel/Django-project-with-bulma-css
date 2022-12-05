from django import forms
from apps.personal.models import Personal



class NewDepartamentoForm(forms.Form):
    first_name = forms.CharField( widget = forms.TextInput(
                attrs={
                    "placeholder": "Ingrese nombre",
                    "class":"input",
                    
                }
            ),label = "Nombre",max_length=50 )
    last_name = forms.CharField(widget = forms.TextInput(
                attrs={
                    "placeholder": "Ingrese apellido",
                    "class":"input",
                    
                }
            ),label = "Apellido",max_length=50)
    departamento = forms.CharField(widget = forms.TextInput(
                attrs={
                    "placeholder": "Ingrese departamento",
                    "class":"input",
                    
                }
            ),label = "Departamento",max_length=50)
    shortname = forms.CharField(widget = forms.TextInput(
                attrs={
                    "placeholder": "Ingrese nombre corto",
                    "class":"input",
                    
                }
            ),label = "Nombre Corto",max_length=20)

    
