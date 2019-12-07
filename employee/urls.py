from django.urls import path, include
from . import views


urlpatterns = [

    path('', views.employee, name='employee'),
    path('addEmployee/', views.add_bd, name='addEmployee/'),
    path('addEmployee/1', views.create, name="addEmployee/1"),
    path('delete/<int:id>/', views.delete, name="delete/"),
    path('edit/<int:id>/', views.edit, name="edit/"),


]