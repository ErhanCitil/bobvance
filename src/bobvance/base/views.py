from bobvance.base.models import Product
from django.views.generic import ListView, DetailView, TemplateView, View
from django.shortcuts import get_object_or_404, render, redirect
from django.http import JsonResponse

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json
<<<<<<< HEAD
from django.contrib import messages
=======
>>>>>>> ea640df87c2bd56b8eb8e0be8e6574928b45380b

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

class CartView(View):
    def get(self, request, *args, **kwargs):
        cart = request.session.get('cart', {})

        product_ids = [pid for pid in cart.keys() if pid is not None and pid != 'null' and pid.isdigit()]

        cart_items = Product.objects.filter(id__in=product_ids)

        total_price = sum([product.price * cart[str(product.id)] for product in cart_items])

        context = {
            'cart_items': [
                {'product': product, 'quantity': cart[str(product.id)]}
                for product in cart_items
            ],
            'total_price': total_price,
        }

        return render(request, 'base/cart.html', context)


class AddToCartView(View):
    def post(self, request, *args, **kwargs):
        product_id = request.POST.get('product_id')
        quantity = int(request.POST.get('quantity', 1))

        cart = request.session.get('cart', {})
        if product_id in cart:
            cart[product_id] += quantity
        else:
            cart[product_id] = quantity

        request.session['cart'] = cart

        return redirect('cart')

class UpdateCartView(View):
    def post(self, request, *args, **kwargs):
        product_id = request.POST.get('product_id')
        quantity = int(request.POST.get('quantity'))

        cart = request.session.get('cart', {})
        if product_id in cart and quantity > 0:
            cart[product_id] = quantity
        elif product_id in cart and quantity <= 0:
            del cart[product_id]

        request.session['cart'] = cart

        return redirect('cart')

class RemoveFromCartView(View):
    def post(self, request, *args, **kwargs):
        product_id = request.POST.get('product_id')
        cart = request.session.get('cart', {})

        if product_id in cart:
            del cart[product_id]
            request.session['cart'] = cart
            status = 'success'
            message = 'Product successfully removed from cart.'
        else:
            status = 'failed'
            message = 'Product not found in cart.'

        if request.is_ajax():
            return JsonResponse({'status': status, 'message': message})

        return redirect('cart')
