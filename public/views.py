from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def index(request):
    template = loader.get_template('public/index.html')
    page_info = {
        "title" : "Home Page",
        "Description" : "It is a free app for data learning developer"
    }
    return HttpResponse(template.render(page_info, request))