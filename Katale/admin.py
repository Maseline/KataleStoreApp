from django.contrib import admin
from .models import Product, Genre,Gender, ProductType

 # Register your models here.

admin.site.register(Product)
admin.site.register(Genre)
admin.site.register(Gender)
admin.site.register(ProductType)