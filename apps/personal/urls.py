from django.contrib import admin
from django.urls import path

from . import views

app_name = "personal_app"

urlpatterns = [
    path('inicio_personal/', views.InicioPersonal.as_view()),
    path('lista_datos_personal/', views.InicioListaDatos.as_view(), name= "personal_all"),
    path('crear_datos_personal/', views.CrearDatoPersonal.as_view()),
    path('lista_empleados_area/<name>', views.ListByAreaEmployee.as_view(), name="personal_departamento"),
    path('lista_empleados_keyword/', views.ListEmployeeByKeyword.as_view()),
    path('lista_skill_empleado/', views.ListSkillsEmployee.as_view()),
    path('detalle_empleado/<pk>', views.DetallePersonal.as_view(), name= "detalle_empleado"),
    path("sumar_personal/", views.SumarPersonal.as_view(), name="add_personal"),
    path("succes/", views.SuccesPersonal.as_view(), name= "succes"),
    path("delete/", views.DeletePersonal.as_view(), name= "delete"),
    path("success_new_personal/", views.Add_Personal.as_view(), name= "new_personal"),
    path("update_personal/<pk>", views.PersonalUpdateView.as_view(), name= "update_personal"),
    path("delete_personal/<pk>", views.PersonalDeleteView.as_view(), name= "delete_personal"),
    path("admin_personal/", views.AdminListaDatos.as_view(), name= "admin_personal"),

]
