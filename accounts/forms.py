from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    full_name = forms.CharField(max_length=255, required=False)
    phone_number = forms.CharField(max_length=15, required=False)
    address = forms.CharField(widget=forms.Textarea, required=False)

    class Meta:
        model = CustomUser
        fields = ('username', 'full_name', 'email', 'phone_number', 'address', 'password1', 'password2')

class CustomLoginForm(AuthenticationForm):
    role = forms.ChoiceField(choices=[('customer', 'Customer'), ('admin', 'Admin')], required=True)
