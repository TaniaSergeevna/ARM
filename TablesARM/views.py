from django.shortcuts import render

# Create your views here.


def tables(request):
    return render(request, 'TablesARM/tables.html')