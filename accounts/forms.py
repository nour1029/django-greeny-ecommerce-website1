from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserAdress


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")


class UserActivateForm(forms.Form):
    code = forms.CharField(max_length=8)




class UserAdressForm(forms.ModelForm):
    class Meta:
        model = UserAdress
        fields = '__all__'
        # exclude = ('user',)
