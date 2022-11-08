from django.views import View
from .models import Productos, Categorias
from django.views.generic.list import ListView
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .forms import UserForm, SellForm,  ProductForm
from django.contrib import messages
# Create your views here.


def home(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())


def contact(request):
    template = loader.get_template('contact.html')
    return HttpResponse(template.render())


class ProductListView(ListView):

    model = Productos
    paginate_by = 100  # if pagination is desired


class ProductView(View):
    model = Productos


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
            messages.success(request, "Compra realizada con éxito")
        else:
            messages.error(request, "Error en la carga de la compra")
    else:
        sell_form = SellForm()
    return render(request, "sell.html", {"sell_form": sell_form})


def product_register(request):
    '''Register a new Product, It has matter the Categories foreign Key '''
    if request.method == "POST":
        product_form = ProductForm(request.POST)
        if product_form.is_valid():
            messages.success(request, "Registro exitoso!")
            product_form = product_form.cleaned_data
            print(product_form)
            product = Productos(nombre_producto=product_form['product_name'],
                                precio=product_form['price'],
                                categoria=Categorias.objects.get(
                                    pk=product_form['category']),
                                stock=product_form['stock'])
            product.save()
        else:
            messages.error(request, "Error al registrar este producto!")
    else:
        product_form = ProductForm()
    return render(request, "product.html", {"product_form": product_form})
