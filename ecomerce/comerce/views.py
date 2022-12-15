from django.views import View
from .models import Productos, Ventas, Mensaje, Categorias
from django.views.generic.list import ListView
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .forms import UserForm, SellForm, ProductForm, MessageForm, CategoryForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db.utils import IntegrityError
from datetime import date, datetime
from django.core import serializers


def home(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())


class ProductListView(ListView):

    model = Productos
    template_name = "index.html"
    paginate_by = 6  # if pagination is desired


class MessageTableView(ListView):

    model = Mensaje
    template_name = "message_list.html"
    paginate_by = 6  # if pagination is desired


class MessageDetailView(View):
    def get(self, request, *args, **kwargs):
        message = Mensaje.objects.get(pk=kwargs['pk'])
        context = {'message': message}
        return render(request, 'message_detail.html', context)


class ProductTableView(ListView):

    model = Productos
    template_name = "product_list.html"
    paginate_by = 6  # if pagination is desired


class SellListView(ListView):
    model = Ventas
    template_name = "sell_list.html"
    paginate_by = 6  # if pagination is desired


def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        print(username, password)
        user = authenticate(
            request=request, username=username, password=password)
        print(user)
        if user is not None:
            form = login(request, user=user)
            messages.success(request, f'Bienvenido {username}')
            print("Formulario valido")
            return redirect('login')
        else:
            messages.error(request, f'Usuario o contraseña incorrecto')
            return redirect('login')
    else:
        form_auth = AuthenticationForm()
    return render(request, "login.html", {"form_user": form_auth})


def contact(request):
    if request.method == "POST":
        contact_form = MessageForm(request.POST)
        user_log = User(request.user)
        if contact_form.is_valid():
            print('Is valid!')
            user_message = Mensaje(usuario=user_log.id,
                                   fecha=datetime.now(),
                                   motivo=contact_form.cleaned_data['motivo'],
                                   mensaje=contact_form.cleaned_data['mensaje'])
            user_message.save()
            messages.success(request, 'Mensaje enviado con éxito!')
            return redirect('contact')
        else:
            print('Is not valid!')
    else:
        contact_form = MessageForm()
    return render(request, "contact.html", {"contact_form": contact_form})


def register(request):
    user_form = UserForm()
    try:
        if request.method == "POST":
            user_form = UserForm(request.POST)
            if user_form.is_valid():
                new_user = User.objects.create_user(username=request.POST['username'],
                                                    first_name=request.POST['name'],
                                                    email=request.POST['email'],
                                                    password=request.POST['password'])
                new_user.save()
                messages.success(request, "Registro exitoso!")
                return redirect('login')
    except IntegrityError as e:
        messages.error(
            request,
            "El usuario o email ingresado ya existen. Por favor ingrese uno distinto!")
    except Exception as e:
        messages.error(
            request,
            "Ha ocurrido un error en el registro. Por favor intente nuevamente!")
    return render(request, "register_user.html", {"user_form": user_form})


@login_required(login_url='login')
def success_sell(request):
    sell = request.session["sell"]
    user = request.user
    user_log = User(user)
    sell_obj = Ventas(
        producto=Productos.objects.get(pk=sell["id_product"]),
        cantidad=sell["quantity"],
        monto=sell["amount"],
        usuario=user_log.id, fecha=date.today())
    result = sell_obj.sell()
    if result:
        sell_obj.save()
        messages.success(request, "Compra Exitosa!")
    else:
        messages.error(request,
                       "La Compra no se ha podido realizar!")

    return render(request, "success_sell.html", {"sell": sell_obj})


@login_required(login_url='login')
def confirm_sell(request):
    sell = request.session['sell'].copy()
    product = Productos.objects.get(pk=sell["id_product"])
    sell["product"] = product
    print(request.session['sell'])
    return render(request, "confirm_sell.html", {"sell": sell})


@login_required(login_url='login')
def sell(request, id_producto=None):
    product = Productos.objects.get(pk=id_producto)
    if request.method == "POST":
        sell_form = SellForm(request.POST)
        if sell_form.is_valid():
            if product.stock >= sell_form.cleaned_data["quantity"]:
                sell = {"id_product": product.pk,
                        "quantity": sell_form.cleaned_data["quantity"],
                        "amount": sell_form.cleaned_data["quantity"] * product.precio,
                        }
                request.session['sell'] = sell
                return redirect('confirm_sell')
            else:
                messages.error(
                    request, "La cantidad supera la disponibilidad.")
        else:
            messages.error(request, "Error en la carga de la compra")
    else:
        sell_form = SellForm()
        #product = Productos.objects.get(pk=id_producto)
    return render(request, "sell.html", {"sell_form": sell_form, "product": product})


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


class CategoryView(View):
    '''Register a new Category '''

    form_class = CategoryForm
    template_name = 'category.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'category_form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Registro exitoso!")
            return redirect('category_register')
        print("Error!!!!", form.cleaned_data)


class CategoryTableView(ListView):

    model = Categorias
    template_name = "category_list.html"
    paginate_by = 6  # if pagination is desired
