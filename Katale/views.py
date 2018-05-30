from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from Katale.forms import RegistrationForm
from .models import ProductType,Product,Gender,Genre


# Create your views here.

def index(request):
    gender = Gender.objects.all()
    product_types = ProductType.objects.all()
    product_genre = Genre.objects.all()
    return render(request, 'Katale/index.html', {"gender": gender, "product_types": product_types, "product_genres": product_genre})

def user_registration(request):
    form = RegistrationForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request, 'Katale/register.html', {'registration_form':form})