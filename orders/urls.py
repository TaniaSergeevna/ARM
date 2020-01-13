from django.urls import path, include
from . import views

urlpatterns = [

    path('', views.order, name='order'),
    path('addOrders/', views.add, name='addOrders/'),
    path('addOrders/1', views.create, name="addOrders/1"),
    path('delete/<int:id>/', views.delete, name="delete/"),
    # path('edit/<int:id>/', views.edit, name="edit/"),

]
