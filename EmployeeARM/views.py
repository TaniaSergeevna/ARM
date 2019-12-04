from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render

from .models import Workers
# Create your views here.


def employee(request):
    people = Workers.objects.all()
    return render(request, 'EmployeeAPM/employee.html', {"people": people})


def add_bd(request):
    people = Workers.objects.all()
    return render(request, 'EmployeeAPM/addEmployee.html', {"people": people})


def create(request):
    if request.method == "POST":
        print(request.POST.get('name'),
                     request.POST.get('surname'),
                      request.POST.get('position'),
                      request.POST.get('phone'),
                      request.POST.get('address'),
                      request.POST.get('worksNumber'))
        tom = Workers(name=request.POST.get('name'),
                      surname=request.POST.get('surname'),
                      position=request.POST.get('position'),
                      phone=request.POST.get('phone'),
                      address=request.POST.get('address'),
                      worksNumber=request.POST.get('worksNumber'))

        tom.save()
    return HttpResponseRedirect("/employee/addEmployee/")


def delete(request, id):
    try:

        person = Workers.objects.get(id=id)
        person.delete()
        return HttpResponseRedirect("/employee/addEmployee/")

    except Workers.DoesNotExist:

        return HttpResponseRedirect("/employee/addEmployee/")


def edit(request, id):
    try:
        person = Workers.objects.get(id=id)
        person.delete()
        if request.method == "POST":
            person.name = request.POST.get("name")
            person.surname = request.POST.get('surname')
            person.position = request.POST.get('position')
            person.phone = request.POST.get('phone')
            person.address = request.POST.get('address')
            person.save()
            return HttpResponseRedirect("/employee/addEmployee/")
        else:
            return render(request, "EmployeeAPM/edit_employee.html", {"person": person})
    except Workers.DoesNotExist:
        return HttpResponseNotFound("/employee/addEmployee/")
