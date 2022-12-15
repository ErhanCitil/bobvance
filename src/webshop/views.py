from django.shortcuts import render
from django.views import generic
from .models import *
# Create your views here.

class Index(generic.ListView):
    template_name = 'webshop/index.html'
    model = Product
    context_object_name = 'producten'