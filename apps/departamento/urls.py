from django.contrib import admin
from django.urls import path
from . import views

app_name = "departamento_app"

urlpatterns = [
    path("", views.IndexView.as_view()),
    path('inicio_departamento/', views.PruebaInicio.as_view()),
    path('lista_departamento/', views.DepaLista.as_view(), name="lista_departamento"),
    path('new_departamento/', views.NewDepartamentoView.as_view(), name= "nuevo_departamento"),
    # path('personal_departamento/<departamento>', views.Personal_departamento_ListView.as_view(), name="personal_departamento"),
    
]

