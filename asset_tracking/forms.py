from django import forms
from .models import Asset
from django.contrib.auth.forms import AuthenticationForm

class AssetForm(forms.ModelForm):
    class Meta:
        model = Asset
        fields = ('name','producer','made_in','status','warranty_date','bienso','note',)

class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username", max_length=30,
                               widget=forms.TextInput(
                                   attrs={'class': 'form-control', 'name': 'username', 'placeholder': 'Username'}))
    password = forms.CharField(label="Password", max_length=30,
                               widget=forms.PasswordInput(
                                   attrs={'class': 'form-control', 'name': 'password', 'placeholder': 'Password'}))