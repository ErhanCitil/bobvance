from django.shortcuts import render
from django.views import generic
from .models import *
from django.shortcuts import get_object_or_404
# Create your views here.

class Index(generic.ListView):
    template_name = 'webshop/index.html'
    model = Product
    context_object_name = 'producten'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['producten'] = Product.objects.all().order_by('?')[:3]
        return context

class ProductSite(generic.DetailView):
    template_name = 'webshop/product.html'
    model = Product
    context_object_name = 'product'

class Assortiment(generic.ListView):
    template_name = 'webshop/assortiment.html'
    model = Product
    context_object_name = 'producten'

    def get_select_new(self):
     if self.request.POST.get('new') == 'new':
        return Product.objects.filter(new=True)

    def get_select_not_new(self):
        if self.request.POST.get('gebruikt') == 'gebruikt':
            return Product.objects.filter(new=False)