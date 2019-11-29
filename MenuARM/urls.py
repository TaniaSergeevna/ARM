from django.urls import path, include
from . import views


urlpatterns = [

    path('', views.menu, name='menu'),
    path('addDB/', views.addDB, name="addDB/"),
    path('addDB/1', views.db, name="addDB/1"),
    path('addDB/delete/<int:id>/', views.delete, name="addDB/delete/"),
    path('addDB/edit/<int:id>/', views.edit, name="addDB/edit/"),


    # path('employee/', views.employee, name='employee'),
    # path('tables/', views.tables, name='tables'),
    # path('suppliers/', views.suppliers, name='suppliers'),
    # # path('addDB/', views.creates, name='addDB')

]