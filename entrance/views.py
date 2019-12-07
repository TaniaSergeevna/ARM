from django.shortcuts import render

from .models import Login
# Create your views here.

from django.http import HttpResponseRedirect, HttpResponseNotFound


def login(request):
    return render(request, 'entrance/login.html')


def homePage(request):
    return render(request, 'entrance/novigation.html')

#
# # def menu(request):
# #     people = Menu1.objects.all()
# #     people1 = Menu2.objects.all()
# #     people2 = Menu3.objects.all()
# #     people3 = Menu4.objects.all()
# #     people4 = Menu5.objects.all()
# #     people5 = Menu6.objects.all()
# #     people6 = Menu7.objects.all()
# #
# #     return render(request, 'menu/menu.html', {"people": people, "people1": people1, "people2": people2, "people3": people3,
# #                                          "people4": people4, "people5": people5, "people6": people6})
# #
# #
# # def suppliers(request):
# #     return render(request, 'suppliers/suppliers.html')
# #
# #
# # def tables(request):
# #     return render(request, 'tables/tables.html')
# #
# #
# # def employee(request):
# #     return render(request, 'employee/employee.html')
# #
# #
# # def addDB(request):
# #     people = Menu1.objects.all()
# #     return render(request, 'menu/addDB.html', {"people": people})
# #
# #
# # def db(request):
# #
# #     if request.method == "POST":
# #         # print(request.path)
# #
# #         tom = Menu1(name=request.POST.get('name'), weight=request.POST.get('weight'),
# #                     price=request.POST.get("price"))
# #         tom.save()
# #     return HttpResponseRedirect("/menu/addDB/")
# #
# #
# # def delete(request, id):
# #     try:
# #
# #         person = Menu1.objects.get(id = id)
# #         person.delete()
# #         return HttpResponseRedirect("/menu/addDB/")
# #
# #     except Menu1.DoesNotExist:
# #
# #         return HttpResponseRedirect("/menu/addDB/")
# #
# #
# # def edit(request, id):
# #     try:
# #         person = Menu1.objects.get(id = id)
# #         person.delete()
# #         if request.method == "POST":
# #             person.name = request.POST.get("name")
# #             person.weight = request.POST.get("weight")
# #             person.price = request.POST.get("price")
# #             person.save()
# #             return HttpResponseRedirect("/menu/addDB/")
# #         else:
# #             return render(request, "menu/edit.html", {"person": person})
# #     except Menu1.DoesNotExist:
# #         return HttpResponseNotFound("/menu/addDB/")
#
#
def entrance(request):

    people = Login.objects.all()
    if request.method == "POST":

        email = request.POST.get('email')
        password = request.POST.get('password')

    for peo in people:
        if peo.email == email and peo.password == password:
            return HttpResponseRedirect("/menu/")
        else:
            return HttpResponseNotFound("<h2>Person not found</h2>")