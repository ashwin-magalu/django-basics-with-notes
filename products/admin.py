from django.contrib import admin

# Register your models here.
from .models import Product # do this only after creating a Model in models.py file and migrating it

admin.site.register(Product) # after adding this, check in admin panel, you can see Products
