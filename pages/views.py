from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):
    print("request:", request.user)
    print("args:", args)
    print("kwargs",kwargs)
    # return HttpResponse("<h1>Hello World!</h1>")
    return render(request, "home.html", {}) 
    # {} --> Empty dictionary/ context, home.html --> template name

def contact_view(request, *args, **kwargs):
    # return HttpResponse("<h1>Contact Page</h1>")
    return render(request, "contact.html", {})

def about_view(request, *args, **kwargs):
    my_context = {
        "my_text": "this is about me",
        "my_number": 123,
        "my_list": [123, 234, 345, "abc", True],
        "my_html": "<h1>Hello folks</h1>"
    }
    return render(request, "about.html", my_context)

def social_view(request, *args, **kwargs):
     return HttpResponse("<h1>Social Page</h1>")