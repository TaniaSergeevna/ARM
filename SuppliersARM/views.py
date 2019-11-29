from django.shortcuts import render


# Create your views here.

def suppliers(request):
    return render(request, 'SuppliersARM/suppliers.html')
