from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from Katale.forms import RegistrationForm

# Create your views here.

def index(request):
    return render(request, 'Katale/index.html', {})


def user_registration(request):
    form = RegistrationForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request, 'Katale/register.html', {'registration_form':form})