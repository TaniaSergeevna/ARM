from django.urls import path, include
from . import views

urlpatterns = [

    path('', views.suppliers, name='suppliers'),
    path('addSuppliers/', views.add_bd, name='addSuppliers/'),
    path('addSuppliers/1', views.create, name="addSuppliers/1"),
    path('delete/<int:id>/', views.delete, name="delete/"),
    path('edit/<int:id>/', views.edit, name="edit/"),
    # path('tables/', views.tables, name='tables'),
    # path('suppliers/', views.suppliers, name='suppliers'),
    # # path('addDB/', views.creates, name='addDB')

]
