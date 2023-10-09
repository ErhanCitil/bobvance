from bobvance.base.models import Product
from django.views.generic import ListView, DetailView, TemplateView, View
from django.shortcuts import get_object_or_404
from django.http import JsonResponse

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

class AddToCartView(View):
    def post(self, request, *args, **kwargs):
        product_id = request.POST.get('product_id')
        product = get_object_or_404(Product, id=product_id)
        cart = request.session.get('cart', {})

        if product_id in cart:
            cart[product_id] += 1
        else:
            cart[product_id] = 1

        request.session['cart'] = cart

        return JsonResponse({'status': 'success'})

class CartView(TemplateView):
    template_name = 'base/cart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart = self.request.session.get('cart', {})
        products_in_cart = Product.objects.filter(id__in=cart.keys())
        total_price = sum([product.price * cart[str(product.id)] for product in products_in_cart])

        context['cart_items'] = [
            {'product': product, 'quantity': cart[str(product.id)]}
            for product in products_in_cart
        ]
        context['total_price'] = total_price
        return context
