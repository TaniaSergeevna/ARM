from django.urls import path, include
from . import views


urlpatterns = [


    # path('employee/', views.employee, name='employee'),
    path('', views.tables, name='tables'),
    # path('suppliers/', views.suppliers, name='suppliers'),
    # # path('addDB/', views.creates, name='addDB')

]