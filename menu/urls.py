from django.urls import path, include
from . import views


urlpatterns = [

    path('', views.menu, name='menu'),
    path('addDB/', views.addDB, name="addDB/"),
    path('addDB/1', views.db, name="addDB/1"),
    path('delete/<int:id>/', views.delete, name="delete/"),
    path('edit/<int:id>/', views.edit, name="edit/"),


    # path('employee/', views.employee, name='employee'),
    # path('tables/', views.tables, name='tables'),
    # path('suppliers/', views.suppliers, name='suppliers'),
    # # path('addDB/', views.creates, name='addDB')

]