from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from .forms import ProductForm, RawProductForm

# Create your views here.
""" def product_detail_view(request):
    obj = Product.objects.get(id=1)
   # context = {
   #    'title': obj.title,
   #    'description': obj.description,
   #    'price': obj.price,
   #    'summary': obj.summary,
   #    'featured': obj.featured,
   #} 
    context = {
        'object': obj
    } 
    # return render(request, "product/detail.html", context)
    return render(request, "products/product_detail.html", context) """
    
""" def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()
    context = {
        'form': form
    } 
    return render(request, "products/product_create.html", context) """

""" def product_create_view(request):
    # print("Get: ",request.GET)
    # print("Post: ",request.POST)
    if request.method == "POST":
        my_new_title = request.POST.get('title')
        # Product.objects.create(title=my_new_title)
        print("Title: ", my_new_title)
    context = {} 
    return render(request, "products/product_create.html", context) """

""" def product_create_view(request):
    my_form = RawProductForm()
    if request.method == "POST":
        my_form = RawProductForm(request.POST)
        if my_form.is_valid():
            # now the data is good
            print(my_form.cleaned_data)
            Product.objects.create(**my_form.cleaned_data)
        else:
            print(my_form.errors)

    context = {
        'form': my_form
    } 
    return render(request, "products/product_create.html", context) """

# For Form validation methods
def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()
    context = {
        'form': form
    } 
    return render(request, "products/product_create.html", context)

# for Initial values for forms
""" def product_create_view(request):
    initial_data={
        'title': "My Awesome Title"
    }
    obj = Product.objects.get(id=1)
    #form = ProductForm(request.POST or None, initial=initial_data, instance=obj)
    form = ProductForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
    context = {
        'form': form
    } 
    return render(request, "products/product_create.html", context) """

# Dynamic URL routing

def product_detail_view(request, my_id):
    # obj = Product.objects.get(id = my_id)
    obj = get_object_or_404(Product, id = my_id) # for Handle does not exist or do as shown below:
    # try:
    #     obj = Product.objects.get(id = my_id)
    # except Product.DoesNotExist:
    #     raise Http404
    context= {
        "object": obj
    }
    return render(request, "products/product_detail.html", context)

# Delete and confirm
def product_delete_view(request, my_id):
    obj = get_object_or_404(Product, id = my_id) 
    # For POST method delete
    if request.method == "POST":
        # Confirming delete
        obj.delete()
        return redirect('../../../')
    # obj.delete() # deletes this object, but this happens in GET Request
    context= {
        "object": obj
    }
    return render(request, "products/product_delete.html", context)

def product_list_view(request):
    querySet = Product.objects.all() # returns a list of objects
    context = {
        "object_list": querySet
    }
    return render(request, "products/product_list.html", context)

def product_update_view(request, id = id):
    obj = get_object_or_404(Product, id=id)
    form = ProductForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
    context = {
        "form": form
    }
    return render(request, "products/product_create.html", context)