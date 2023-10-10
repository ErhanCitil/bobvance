from bobvance.base.models import Product
from django.views.generic import ListView, DetailView, TemplateView, View
from django.shortcuts import get_object_or_404
from django.http import JsonResponse

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json

class Home(TemplateView):
    template_name = 'base/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.order_by('?')[:5]
        return context

class ProductsView(ListView):
    model = Product
    template_name = 'base/products.html'

class ProductDetailView(DetailView):
    model = Product
    template_name = 'base/product_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['more_products'] = Product.objects.exclude(pk=self.object.pk).order_by('?')[:5]
        return context
