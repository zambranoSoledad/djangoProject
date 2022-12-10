from django import forms
from django.forms import ValidationError, ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import Productos, User

# Validador para no ingresar compras con cantidad de productos erronea


def quantity_products_validate(value):
    if not value or value < 1:
        raise ValidationError(
            "Debes ingresar al menos 1 producto en la compra",
            code="error_quantity_products",)


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
        attrs={'class': 'form-control m-2 p-2'}),
        label="Contraseña")

    # def clean_user(self):
    #    data = self.cleaned_data['password']
    #    if len(data) < 3:  # solo es prueba
    #        print("Password very short!")
    #        raise ValidationError("Too short password!")
    #    return data

# class UserRegisterForm(forms.Form):

#     # forms.CharField(widget=forms.TextInput(attrs={"class":"css_class"}))
#     name = forms.CharField(widget=forms.TextInput(
#         attrs={'class': 'form-control m-2 p-2'}), label="Nombre", required=True)
#     lastName= forms.CharField(widget=forms.TextInput(
#         attrs={'class': 'form-control m-2 p-2'}), label="Nombre", required=False)
#     email = forms.EmailField(widget=forms.TextInput(
#         attrs={'class': 'form-control m-2 p-2'}), label="Mail",required=True)
#     username = forms.CharField(widget=forms.TextInput(
#         attrs={'class': 'form-control m-2 p-2'}), label="Usuario")
#     password = forms.CharField(widget=forms.PasswordInput(
#         attrs={'class': 'form-control m-2 p-2'}),
#         label="Contraseña")


class SellForm(forms.Form):

    # username = forms.CharField(widget=forms.TextInput(
    #    attrs={'class': 'form-control m-2 p-2'}), label="Usuario", required=True)
    # date = forms.DateField(widget=forms.SelectDateWidget(
    #    attrs={'class': 'form-control m-2 p-2'}), label="Fecha", required=True)
    # product = forms.CharField(widget=forms.TextInput(
    #    attrs={'class': 'form-control m-2 p-2'}), label="Producto")
    quantity = forms.IntegerField(widget=forms.NumberInput(
        attrs={'class': 'form-control m-2 p-2'}), label="Cantidad", validators=(quantity_products_validate,))


class ProductForm(ModelForm):
    class Meta:
        model = Productos
        fields = '__all__'
