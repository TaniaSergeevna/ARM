from django.shortcuts import render

from .models import Menu1, Menu2, Menu3, Menu4, Menu5, Menu6, Menu7

from django.http import HttpResponseRedirect, HttpResponseNotFound


def menu(request):
    people = Menu1.objects.all()
    people1 = Menu2.objects.all()
    people2 = Menu3.objects.all()
    people3 = Menu4.objects.all()
    people4 = Menu5.objects.all()
    people5 = Menu6.objects.all()
    people6 = Menu7.objects.all()

    return render(request, 'menu/menu.html',
                  {"people": people, "people1": people1, "people2": people2, "people3": people3,
                   "people4": people4, "people5": people5, "people6": people6})


def addDB(request):
    people = Menu1.objects.all()
    return render(request, 'menu/addDB.html', {"people": people})


def db(request):
    if request.method == "POST":
        print()

        tom = Menu1(name=request.POST.get('name'),
                    weight=request.POST.get('weight'),
                    price=request.POST.get("price"))
        tom.save()
    return HttpResponseRedirect("/menu/addDB/")


def delete(request, id):
    try:

        person = Menu1.objects.get(id=id)
        person.delete()
        return HttpResponseRedirect("/menu/addDB/")

    except Menu1.DoesNotExist:

        return HttpResponseRedirect("/menu/addDB/")


def edit(request, id):
    try:
        person = Menu1.objects.get(id=id)
        person.delete()
        if request.method == "POST":
            person.name = request.POST.get("name")
            person.weight = request.POST.get("weight")
            person.price = request.POST.get("price")
            person.save()
            return HttpResponseRedirect("/menu/addDB/")
        else:
            return render(request, "menu/edit.html", {"person": person})
    except Menu1.DoesNotExist:
        return HttpResponseNotFound("/menu/addDB/")


