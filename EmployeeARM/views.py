from django.shortcuts import render

from .models import HallWorkers, KitchenWorkers, Administrator
# Create your views here.


def employee(request):
    people = HallWorkers.objects.all()
    people1 = KitchenWorkers.objects.all()
    people2 = Administrator.objects.all()
    return render(request, 'EmployeeAPM/employee.html',{"people": people, "people1": people1, "people2": people2})
