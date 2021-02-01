from django.http import HttpResponse
from django.shortcuts import redirect, render

# Create your views here.
def index(request):
    return render(request, "hello/index.html")

def gabriel(request):
    return HttpResponse("I'm still stand, yeah yeah yeah")

def greet(request, name):
    return render(request, "hello/greet.html", {
         "name": name.capitalize()
    })