from django import forms
from django.forms import ValidationError

from .models import Productos

# Validador para no ingresar compras con cantidad de productos erronea


def quantity_products_validate(value):
    if not value or value < 0:
        raise ValidationError(
            "Debes ingresar al menos 1 producto en la compra", code="error_quantity_products",)

class ContactForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control m-2 p-2'}), label="Nombre",)
    apellido = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control m-2 p-2'}), label="Apellido",)
    email = forms.EmailField(widget=forms.TextInput(
        attrs={'class': 'form-control m-2 p-2'}), label="Mail")
    textarea = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control m-2 p-5'}), label="Textarea",)

class UserForm(forms.Form):

    # forms.CharField(widget=forms.TextInput(attrs={"class":"css_class"}))
    name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control m-2 p-2'}), label="Nombre", required=False)
    email = forms.EmailField(widget=forms.TextInput(
        attrs={'class': 'form-control m-2 p-2'}), label="Mail")
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control m-2 p-2'}), label="Usuario")
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control m-2 p-2'}), label="Contraseña")

    # def clean_user(self):
    #    data = self.cleaned_data['password']
    #    if len(data) < 3:  # solo es prueba
    #        print("Password very short!")
    #        raise ValidationError("Too short password!")
    #    return data


class SellForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control m-2 p-2'}), label="Usuario", required=True)
    date = forms.DateField(widget=forms.SelectDateWidget(
        attrs={'class': 'form-control m-2 p-2'}), label="Fecha", required=True)
    product = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control m-2 p-2'}), label="Producto")
    quantity = forms.IntegerField(widget=forms.NumberInput(
        attrs={'class': 'form-control m-2 p-2'}), label="Cantidad", validators=(quantity_products_validate,))
    amount = forms.FloatField(widget=forms.NumberInput(
        attrs={'class': 'form-control m-2 p-2'}), label="Monto")


class ProductForm(forms.Form):
    product_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control m-2 p-2'}), label="Descripción", required=True)
    category = forms.IntegerField(widget=forms.NumberInput(
        attrs={'class': 'form-control m-2 p-2'}), label="Categoria", required=True)
    stock = forms.IntegerField(widget=forms.NumberInput(
        attrs={'class': 'form-control m-2 p-2'}), label="Cantidad", required=True)
    price = forms.FloatField(widget=forms.NumberInput(
        attrs={'class': 'form-control m-2 p-2'}), label="Precio", required=True)
