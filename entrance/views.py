from django.shortcuts import render

from .models import Logins
# Create your views here.

from django.http import HttpResponseRedirect, HttpResponseNotFound


def login(request):
    return render(request, 'entrance/login.html')


def homePage(request):
    return render(request, 'entrance/homePage.html')


def entrance(request):
    people = Logins.objects.all()
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

    for peo in people:

        if peo.email == email and peo.password == password:
            if email == 'admin' and password == 'admin':
                return HttpResponseRedirect("/homePage/")
            elif email == 'test' and password == 'test':
                return HttpResponseRedirect("/orders/")
            else:
                return HttpResponseNotFound("<h2>Неправильные !</h2>")

    else:
            return HttpResponseNotFound("<h2>Неправильные данные повторите ввод!</h2>")
