from django import forms
from .models import Asset,Driver,History
from django.contrib.auth.forms import AuthenticationForm
from crispy_forms.helper import FormHelper
from crispy_forms import layout, bootstrap
from django.forms import inlineformset_factory

class DriverForm(forms.ModelForm):
    class Meta:
        model = Driver
        fields = ('name','license','address','identity',)

class AssetForm(forms.ModelForm):
    class Meta:
        model = Asset
        fields = ('name','producer','made_in','status','warranty_date','bienso','Madriver',)

class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username", max_length=30,
                               widget=forms.TextInput(
                                   attrs={'class': 'form-control', 'name': 'username', 'placeholder': 'Username'}))
    password = forms.CharField(label="Password", max_length=30,
                               widget=forms.PasswordInput(
                                   attrs={'class': 'form-control', 'name': 'password', 'placeholder': 'Password'}))


class HistoryForm(forms.ModelForm):
    class Meta:
        model = History
        fields = ('ngay','congviec','gia','maasset',)

