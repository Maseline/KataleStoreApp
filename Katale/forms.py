from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistrationForm(UserCreationForm):
    attrs = {'class': 'form-control'}
    email = forms.EmailField(max_length=100,widget=forms.EmailInput(attrs=attrs))
    first_name = forms.CharField(widget=forms.TextInput(attrs=attrs))
    last_name =  forms.CharField(widget=forms.TextInput(attrs=attrs))
    password1 = forms.CharField(label="Password",widget=forms.PasswordInput(attrs=attrs),help_text="Your password must contain at least 8 characters."
                                                                                                   "Your password "
                                                                                                   "should not be "
                                                                                                   "entirely numeric "
                                                                                                   "or a commonly "
                                                                                                   "used password")
    password2 = forms.CharField(label="Re-enter Password", widget=forms.PasswordInput(attrs=attrs))
    username = forms.CharField( widget=forms.TextInput(attrs=attrs))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')



