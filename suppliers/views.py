from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render
from .models import Supply


# Create your views here.

def suppliers(request):
    suppli = Supply.objects.all()

    return render(request, 'suppliers/suppliers.html', {'suppli': suppli})


def add_bd(request):
    people = Supply.objects.all()
    return render(request, 'suppliers/addSuppliers.html', {"people": people})


def create(request):
    if request.method == "POST":
        tom = Supply(name=request.POST.get('name'),
                     type_supply=request.POST.get('type_supply'),
                     phone=request.POST.get('phone'),
                     address=request.POST.get('address'))
        tom.save()
    return HttpResponseRedirect("/suppliers/")


def delete(request, id):
    try:

        person = Supply.objects.get(id=id)
        person.delete()
        return HttpResponseRedirect("/suppliers/")

    except Supply.DoesNotExist:

        return HttpResponseRedirect("/suppliers/")


def edit(request, id):
    try:
        person = Supply.objects.get(id=id)
        person.delete()
        if request.method == "POST":
            person.name = request.POST.get("name")
            person.type_supply = request.POST.get('type_supply')
            person.phone = request.POST.get('phone')
            person.address = request.POST.get('address')
            person.save()
            return HttpResponseRedirect("/suppliers/")
        else:
            return render(request, "suppliers/edit_suppliers.html", {"person": person})
    except Supply.DoesNotExist:
        return HttpResponseNotFound("/suppliers/")
