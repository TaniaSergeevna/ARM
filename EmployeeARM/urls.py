from django.urls import path, include
from . import views


urlpatterns = [

    path('', views.employee, name='employee'),
    path('addEmployee/', views.add_bd, name='addEmployee/'),
    path('addEmployee/1', views.create, name="addEmployee/1"),
    path('addEmployee/delete/<int:id>/', views.delete, name="addEmployee/delete/"),
    path('addEmployee/edit/<int:id>/', views.edit, name="addEmployee/edit/"),


]