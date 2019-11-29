from django.urls import path , include
from . import views

urlpatterns = [

    path('', views.login, name='login'),
    path('homePage/', views.homePage, name='homePage'),

    path('menu/', include('MenuARM.urls')),
    path('suppliers/', include('SuppliersARM.urls')),
    path('employee/', include('EmployeeARM.urls')),
    path('tables/', include('TablesARM.urls')),

    path('1/', views.entrance, name='1/')

]