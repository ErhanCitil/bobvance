from django.shortcuts import render
from bobvance.base.models import Product
from django.views.generic import ListView, DetailView, TemplateView

class Home(TemplateView):
    template_name = 'base/index.html'

class ProductsView(ListView):
    model = Product
    template_name = 'base/products.html'

class ProductDetailView(DetailView):
    model = Product
    template_name = 'base/product_detail.html'
    