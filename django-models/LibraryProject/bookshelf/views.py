from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.

def homepage(request):
    template = "bookshelf/home.html/"
    return render(request, template_name=template, context={})

def randompage(request):
    return HttpResponse("<h1>Nothing to see here</h1>")
