from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def home(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def contact(request):
    template = loader.get_template('contact.html')
    return HttpResponse(template.render())

def link(request):
    template = loader.get_template('link.html')
    return HttpResponse(template.render())