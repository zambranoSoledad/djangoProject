from django.views import View
from .models import Productos, Categorias
from django.views.generic.list import ListView
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .forms import UserForm, SellForm, ProductForm, ContactForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.


def home(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())


class ProductListView(ListView):

    model = Productos
    paginate_by = 100  # if pagination is desired


def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(
            request=request, username=username, password=password)
        if user is not None:
            form = login(request, user=user)
            messages.success(request, f'Bienvenido {username}')
            print("Formulario valido")
            return redirect('login')
        else:
            messages.error(request, f'Usuario o contraseña incorrecto')
    else:
        form_auth = AuthenticationForm()
    return render(request, "login.html", {"form_user": form_auth})


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


class ProductView(View):
    '''Register a new Product, It has matter the Categories foreign Key '''

    form_class = ProductForm
    template_name = 'product.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'product_form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Registro exitoso!")
            return redirect('product_register')
        print("Error!!!!", form.cleaned_data)

    '''
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

    '''
