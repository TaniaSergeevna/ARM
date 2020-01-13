from django.shortcuts import render
from orders.models import Orders
# Create your views here.


def tables(request):
    order = Orders.objects.all()
    return render(request, 'tables/tables.html',{'order': order})