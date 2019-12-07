from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render

from .models import Workers
# Create your views here.


def employee(request):
    people = Workers.objects.all()
    return render(request, 'employee/employee.html', {"people": people})


def add_bd(request):
    people = Workers.objects.all()
    return render(request, 'employee/addEmployee.html', {"people": people})


def create(request):
    if request.method == "POST":
        tom = Workers(name=request.POST.get('name'),
                      surname=request.POST.get('surname'),
                      position=request.POST.get('position'),
                      phone=request.POST.get('phone'),
                      address=request.POST.get('address'))

        tom.save()
    return HttpResponseRedirect("/employee/")


def delete(request, id):
    try:

        person = Workers.objects.get(id=id)
        person.delete()
        return HttpResponseRedirect("/employee/")

    except Workers.DoesNotExist:

        return HttpResponseRedirect("/employee/")


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
            return HttpResponseRedirect("/employee/")
        else:
            return render(request, "employee/edit_employee.html", {"person": person})
    except Workers.DoesNotExist:
        return HttpResponseNotFound("/employee/")
