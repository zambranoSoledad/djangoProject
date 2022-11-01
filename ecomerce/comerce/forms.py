from django import forms
from django.forms import ValidationError


class UserForm(forms.Form):

    # forms.CharField(widget=forms.TextInput(attrs={"class":"css_class"}))
    name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control m-2 p-2'}), label="First Name", required=False)
    email = forms.EmailField(widget=forms.TextInput(
        attrs={'class': 'form-control m-2 p-2'}), label="Email")
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control m-2 p-2'}), label="Username")
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control m-2 p-2'}), label="Password")

    # def clean_user(self):
    #    data = self.cleaned_data['password']
    #    if len(data) < 3:  # solo es prueba
    #        print("Password very short!")
    #        raise ValidationError("Too short password!")
    #    return data
