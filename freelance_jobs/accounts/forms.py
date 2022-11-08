from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.contrib.auth.models import User


class RegistrationForm(UserCreationForm):
    username = forms.CharField(label='Username', required=True, min_length=4, max_length=255, widget=forms.TextInput(attrs={'class': 'input-form form-large'}))
    # email = forms.EmailField(label='Email', required=True, min_length=4, max_length=255, widget=forms.TextInput(attrs={'class': 'input-form form-large'}))
    # first_name = forms.CharField(label='First name', required=False, max_length=255, widget=forms.TextInput(attrs={'class': 'input-form form-large'}))
    # last_name = forms.CharField(label='Last name', required=False, max_length=255, widget=forms.TextInput(attrs={'class': 'input-form form-large'}))
    password1 = forms.CharField(label='Password', required=True, widget=forms.PasswordInput(attrs={'class': 'input-form form-large', 'autocomplete': 'new-password'}))
    password2 = forms.CharField(label='Password confirmation', required=True, widget=forms.PasswordInput(attrs={'class': 'input-form form-large', 'autocomplete': 'new-password'}))

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')


class LoginForm(AuthenticationForm):
    username = UsernameField(label='Username', widget=forms.TextInput(attrs={'class': 'input-form form-large', 'autofocus': True}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'input-form form-large', 'autocomplete': 'current-password'}))
