from django.urls import path, include
from . import views

urlpatterns = [

    path('', views.suppliers, name='suppliers'),
    # path('tables/', views.tables, name='tables'),
    # path('suppliers/', views.suppliers, name='suppliers'),
    # # path('addDB/', views.creates, name='addDB')

]