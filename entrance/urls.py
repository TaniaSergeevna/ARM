from django.urls import path, include
from . import views

urlpatterns = [

    path('catalog/', views.login, name='login'),
    path('homePage/', views.homePage, name='homePage'),

    path('menu/', include('menu.urls')),
    path('suppliers/', include('suppliers.urls')),
    path('employee/', include('employee.urls')),
    path('tables/', include('tables.urls')),
    path('orders/', include('orders.urls')),
    path('catalog/1/', views.entrance, name='1/')

]
