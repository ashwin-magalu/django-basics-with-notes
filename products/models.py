from django.db import models
from django.urls import reverse

# Create your models here.
""" class Product(models.Model): # we are inheriting from Model
    title = models.TextField()
    description = models.TextField()
    price = models.TextField()
    summary = models.TextField(default = "This is cool!") """

# https://docs.djangoproject.com/en/2.0/ref/models/fields/#field-types

class Product(models.Model): # we are inheriting from Model
    title = models.CharField(max_length=120) # when CharField is used, max_length is mandatory
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=100)
    summary = models.TextField(blank=True, null=False)
    featured = models.BooleanField(default=False) # null=True, default=True

# Dynamic linking of URLs
def get_absolute_url(self):
    # return f"/products/{self.id}" # for Dynamic linking of URLs
    return reverse("products:product-detail", kwargs={"id": self.id}) # for django URLs reverse