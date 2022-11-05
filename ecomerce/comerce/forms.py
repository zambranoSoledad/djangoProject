from django import forms
#from django.forms import ValidationError


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
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control m-2 p-2'}), label="Usuario", required=True) 
    date = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control m-2 p-2'}), label="Fecha", required=True)
    product = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control m-2 p-2'}), label="Producto")
    quantity = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control m-2 p-2'}), label="Cantidad")
    amount =  forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control m-2 p-2'}), label="Monto")