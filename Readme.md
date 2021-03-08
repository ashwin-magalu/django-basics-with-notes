# Python Django Basics

1. Download Python3 from python.org/downloads
2. Install pip(Python Package Index): python -m pip install -U pip
3. Install virtual environment: pip install virtualenv
4. Set up virtual environment: python -m virtualenv ./ or virtualenv . or virtualenv virtualenvName
5. Get inside Scripts folder: cd Scripts
6. Activate virtual environment: activate (5 and 6 works in windows. source bin/activate works in macOS)
7. Install django: pip install django
8. To deactivate virtual environment: deactivate

## Creating a django project within a virtual environment:

1. To see django and python versions installed in virtual environment: pip freeze
2. To see django core commands: django-admin
3. To create new django project: django-admin startproject projectName . [here, it is trydjango]
4. To start the server: python manage.py runserver [opens in localhost:8000]
5. To run our DB and sync our settings to DB: python manage.py migrate
6. To create an admin: python manage.py createsuperuser [enter name, email and password when prompted]
7. Visit localhost:8000/admin to login and see admin dashboard

## Creating a django app within a virtual environment:

1. To create a new app: python manage.py startapp appName [here, it is products]
2. Edit models.py of the app you created
3. Add appName onto INSTALLED_APPS array within settings.py file(Inside project folder)
4. Run commands: python manage.py makemigrations and python manage.py migrate
5. Repeat step 4 each time you modify models.py file

## Creatingproduct objects in the python shell:

1. Be in root folder and run the command: python manage.py shell [this will allow all django project stuffs to work inside the python interpreter]
2. Run commands:
   from products.models import Product
   Product.objects.all()
   Product.objects.create(title="", description="",...)

## Creating a new model fields:

1. Delete all the files in the migrations folder within your app
2. Delete db.sqlite3 file from root
3. Modify models.py file
4. Create db.sqlite3 file in root
5. Run commands:
   python manage.py makemigrations
   python manage.py migrate
   python manage.py createsuperuser

## Changing a model without deleting migrations folder or db.sqlite3 file:

1. Modify models.py
2. Run commands:
   python manage.py makemigrations
   python manage.py migrate

## Default homepage to custom homepage:

1. Create a new app: python manage.py startapp pages
2. Edit views.py file within pages app
3. Add new app name onto INSTALLED_APPS array within settings.py file(Inside project folder)
4. import function created in views.py file to urls.py file(within project folder) and add it to urlpatterns array

## URL routing and requests:

1. Repeat steps 2 to 4 of Default homepage to custom homepage

## django templates:

1. Instead of returning HttpResponse, return render() of django.shortcuts
2. Create a new folder called templates within your project folder
3. Go to settings.py file and add our template location to DIRS array(within TEMPLATES array) as shown below:
   DIRS: [os.path.join(BASE_DIR, "templates")]

## django templating engine basics:

1. Create a root html page (here, base.html) within templates folder
2. In base.html, create a basic html code and within its body tag, add a following line:
   {% block content %} {% endblock %}
3. Now add {% extends 'base.html' %} at the beginning of all template html file's and wrap all code's within them between: {% block content %} html code {% endblock %}
4. This makes all templates in django uniform
5. Here, content is a reference name, we can give any name we want, but we have to use the same name in templates as well

## Include template tag:

1. Create a new html page(here, navbar.html)
2. Include this file within our base.html file's body tag, before {% block content %} {% endblock %}, as {% include 'navbar.html %}

## Rendering context in a template:

1. Create a context/dictionary with key-value pair in views.py
2. Pass context/directory in views.py
3. use {{}} to display context data. Here, you have to call context key's within {{}}

## For loop in template:

1. In context, create an array of elements. Here, it is called as my_list
2. In template, use forloop to show it in following way:
<ul>
{% for my_sub_list in my_list %}
<li>{{forloop.counter}} - {{my_sub_item}}</li>
{% endfor %}
</ul>

## Using conditions in a template and Template tags and filters:

1. Check about.html file in templates folder of project to know how it works

## Render data from the DB with a model:

1. See product/detail.html file within templates folder of project to know how it works

## How django templates load with apps:

1. Create templates folder within products app
2. Create products sub folder within this templates folder
3. Create products_detail.html file within products folder
4. Add this in views.py file within products app.

## django model forms

1. Create a file named forms.py in products folder
2. Create ProductForm class in that file
3. Create a product_create_view method in views.py file and use ProductForm class in this method
4. Create a new url in urls.py file, called create/
5. Create product_create.html file in templates/products folder within products app folder

## Raw HTML Form

1. In product_create.html file, remove django related stuff like {% csrf_token %} and {{form.as_p}}
2. Comment product_create_view method in views.py file and create a new method with same name
3. Comment out old html code in product_create.html file and add new html code

## Pure django forms

1. Comment product_create_view method in views.py file and create a new method with same name
2. Add a new class in forms.py file, called RawProductForm
3. Comment out old html code in product_create.html file and add new html code

## Form widgets

1. Check forms.py, whatever written within parenthesis are widgets

## Form validation methods

1. Add new fields in forms.py, check that out
2. Comment product_create_view method in views.py file and create a new method with same name

## Initial values for forms

1. Comment product_create_view method in views.py file and create a new method with same name

## Dynamic URL routing

1. Comment product_detail_view method in views.py file and create a new method with same name
2. Edit product url in urls.py file

## Handle does not exist

1. Import get_object_or_404 from django.shortcuts in views.py
2. Import Http404 from django.http in views.py

## Delete and confirm

1. Import redirect from django.http in views.py
2. Create a html file named product_delete.html in products folder
3. Create product_delete_view() in views.py file
4. Add a deleting url to urls.py file

## View of a list of DB Objects

1. Create a product_list_view() in views.py file
2. Create a file product_list.html in products folder
3. Add a listing url to urls.py file

## Dynamic linking of URLs

1. Add a link to instance.title in product_list.html file. This is one way of doing this
2. Other method is: Add one function in models.py file, called get_absolute_url()

## django URLs reverse

1. Import reverse from django.urls
2. Change the return statement in get_absolute_url() within models.py page

## In app URLs and Namespacing

1. Changes are made in urls.py and also urls.py file is created in products folder

## Class based views - List view

1. Create a new app with name blog
2. Check the code there
