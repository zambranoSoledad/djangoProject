from django.views import View
from .models import Productos, Categorias
from django.views.generic.list import ListView
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .forms import UserForm, SellForm, ProductForm, ContactForm
from django.contrib import messages
# Create your views here.


def home(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

class ProductListView(ListView):

    model = Productos
    paginate_by = 100  # if pagination is desired


class ProductView(View):
    model = Productos


def contact(request):
    if request.method == "POST":
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            print("Formulario valido")
    else:
        contact_form = ContactForm()
    return render(request, "contact.html", {"contact_form": contact_form})


def register(request):
    if request.method == "POST":
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            print("Formulario valido")
    else:
        user_form = UserForm()
    return render(request, "register_user.html", {"user_form": user_form})


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
            try:
                product_form = product_form.cleaned_data
                category = Categorias.objects.get(
                    pk=product_form['category'])
                product = Productos(nombre_producto=product_form['product_name'],
                                    precio=product_form['price'],
                                    categoria=category,
                                    stock=product_form['stock'])
                product.save()
                messages.success(request, "Registro exitoso!")
            except Categorias.DoesNotExist as e:
                print(f'Exception: {e.__class__.__name__}')
                messages.error(request, 'Categoria no Encontrada!')
        else:
            messages.error(request, "Error al registrar este producto!")
    else:
        product_form = ProductForm()
    return render(request, "product.html", {"product_form": product_form})
