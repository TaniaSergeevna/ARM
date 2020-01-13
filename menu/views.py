from django.shortcuts import render

from .models import Menu
    # , Sections

from django.http import HttpResponseRedirect, HttpResponseNotFound


def menu(request):
    people = Menu.objects.all()
    return render(request, 'menu/menu.html', {"people": people})


def addDB(request):
    people = Menu.objects.all()
    # sections = Sections.objects.all()
    return render(request, 'menu/addDB.html', {"people": people})


def db(request):
    if request.method == "POST":
        tom = Menu(name=request.POST.get('name'),
                   menu_section=request.POST.get('menu_section'),
                   weight=request.POST.get('weight'),
                   price=request.POST.get('price'))
        tom.save()
    return HttpResponseRedirect("/menu/")


def delete(request, id):
    try:

        person = Menu.objects.get(id=id)
        person.delete()
        return HttpResponseRedirect("/menu/")

    except Menu.DoesNotExist:

        return HttpResponseRedirect("/menu/")


def edit(request, id):
    try:
        person = Menu.objects.get(id=id)
        person.delete()
        if request.method == "POST":
            person.name = request.POST.get("name")
            person.menu_section = request.POST.get("menu_section")
            person.weight = request.POST.get("weight")
            person.price = request.POST.get("price")
            person.save()
            return HttpResponseRedirect("/menu/")
        else:
            return render(request, "menu/edit.html", {"person": person})
    except Menu.DoesNotExist:
        return HttpResponseNotFound("/menu/")

