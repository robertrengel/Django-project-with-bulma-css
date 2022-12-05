from django import forms

from .models import Personal

class PersonalForm(forms.ModelForm):
    """Form definition for Personal."""

    class Meta:
        """Meta definition for Personalform."""

        model = Personal
        fields = [
        'first_name',
        'last_name',
        'job',
        'departamento',
        'skill',
        'image',
    ]
        widgets = {
            "first_name": forms.TextInput(
                attrs={
                    "placeholder": "Ingrese nombre",
                    "class":"input",
                    
                }
            ),
            "last_name": forms.TextInput(
                attrs={
                    "placeholder": "Ingrese apellido",
                    "class":"input",
                    
                }
            ),
            "skill": forms.SelectMultiple(
                attrs={
                    "size": 8,
                    # "class":"input",
                    
                }
            ),
            "image": forms.FileInput(
                attrs={
                    # "size": 8,
                    "class":"file-input",
                    
                }
            ),

        }


# El metodo siguiente define la manera de hacer una comprobacion de los campos
# hay que tener especial cuidado con la definicion de los nombre en las variables
# todo debe hacer referencia al elemento que se quiere validar

    def clean_first_name(self):
        first_name = self.cleaned_data["first_name"]
        if first_name == "nombre":
            raise forms.ValidationError("Ingrese un numero mayor a 10")
        
        return first_name
