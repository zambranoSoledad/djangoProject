from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from comerce.forms import UserForm
from comerce.forms import SellForm #esto el VSC me lo muestra como error

# Create your views here.


def home(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())


def contact(request):
    template = loader.get_template('contact.html')
    return HttpResponse(template.render())


def register(request):
    if request.method == "POST":
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            print("Formulario valido")
    else:
        user_form = UserForm()
    return render(request, "register_user.html", {"user_form": user_form})


def link(request):
    template = loader.get_template('link.html')
    return HttpResponse(template.render())


def sell(request):
    if request.method == "POST":
        sell_form = SellForm(request.POST)
        if sell_form.is_valid():
            print("Formulario valido")
    else:
        sell_form = SellForm()
    return render(request, "sell.html", {"sell_form": sell_form})