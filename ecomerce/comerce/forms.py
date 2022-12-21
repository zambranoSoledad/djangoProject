from django import forms
from django.forms import ValidationError, ModelForm
from .models import Productos, User, Categorias


def quantity_products_validate(value):
    """validate the quantity of the product stock"""
    if not value or value < 1:
        raise ValidationError(
            "Debes ingresar al menos 1 producto en la compra",
            code="error_quantity_products",)


def password_validator(string):
    """validate the password's length"""
    if len(string) < 5:
        raise ValidationError(
            "Contraseña demasiado corta. Debe contener almenos 5 caracteres.",
            code="error_password_length",)


class MessageForm(forms.Form):
    motivo = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control m-2 p-2'}), label="Motivo", required=False)
    mensaje = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'form-control m-2 p-2'}), label="Mensaje")


class UserForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control m-2 p-2'}), label="Nombre", required=False)
    email = forms.EmailField(widget=forms.TextInput(
        attrs={'class': 'form-control m-2 p-2'}), label="Mail")
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control m-2 p-2'}), label="Usuario")
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control m-2 p-2'}),
        label="Contraseña", validators=[password_validator])


class SellForm(forms.Form):
    quantity = forms.IntegerField(widget=forms.NumberInput(
        attrs={'class': 'form-control m-2 p-2'}),
        label="Cantidad",
        validators=(quantity_products_validate,))


class ProductForm(ModelForm):
    class Meta:
        model = Productos
        fields = '__all__'
        widgets = {
            'nombre_producto': forms.TextInput({'class': 'form-control m-2 p-2'}),
            'categoria': forms.Select({'class': 'form-control m-2 p-2'}),
            'precio': forms.NumberInput(
                {'class': 'form-control m-2 p-2'}),
            'stock': forms.NumberInput(
                {'class': 'form-control m-2 p-2'}),

        }


class CategoryForm(ModelForm):

    class Meta:
        model = Categorias
        fields = '__all__'
        widgets = {
            'nombre_categoria': forms.TextInput({'class': 'form-control m-2 p-2'}),
            'descripcion_categoria': forms.TextInput({'class': 'form-control m-2 p-2'}),

        }


class EmailForm(forms.Form):
    subject = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control m-2 p-2'}), label="Motivo")
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control m-2 p-2'}), label="Mensaje")
    sender = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control m-2 p-2'}),label="Email")
    cc_myself = forms.BooleanField(required=False)