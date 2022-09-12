from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=150, label="Nom d'utilisateur")
    first_name = forms.CharField(label="Nom",max_length=30, required=False, help_text="Optionnel")
    last_name = forms.CharField(label="Post-Nom",max_length=30, required=False, help_text="Optionnel")
    email = forms.EmailField(max_length=255, help_text="Obligatoire")
    password1 = forms.CharField(max_length=255, widget=forms.PasswordInput, label="Mot de passe")
    password2 = forms.CharField(max_length=255, widget=forms.PasswordInput, label="Confirmation du Mot de passe")

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)