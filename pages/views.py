from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request,*args,**kwargs):
    print(args,kwargs)
    print(request.user)
    my_context = {
        "title": "This is me",
        "my_number": 123,
        "my_list":[123,124,125,'abc'],
        "my_html":"<h1>Hello World</h1>"
    }
    return render(request,'home.html',my_context)