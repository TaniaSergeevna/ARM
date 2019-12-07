from django.urls import path , include
from . import views

urlpatterns = [

    path('', views.login, name='login'),
    path('homePage/', views.homePage, name='homePage'),

    path('menu/', include('menu.urls')),
    path('suppliers/', include('suppliers.urls')),
    path('employee/', include('employee.urls')),
    path('tables/', include('tables.urls')),

    path('1/', views.entrance, name='1/')

]