from django import forms
from django.forms import ValidationError


class UserForm(forms.Form):

    # forms.CharField(widget=forms.TextInput(attrs={"class":"css_class"}))
    name = forms.CharField(label="First Name", required=False)
    email = forms.EmailField(label="Email")
    username = forms.CharField(label="Username")
    password = forms.CharField(widget=forms.PasswordInput(), label="Password")

    # def clean_user(self):
    #    data = self.cleaned_data['password']
    #    if len(data) < 3:  # solo es prueba
    #        print("Password very short!")
    #        raise ValidationError("Too short password!")
    #    return data
