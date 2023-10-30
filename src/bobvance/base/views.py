from bobvance.base.models import Product, Order, OrderProduct, Customer
from django.views.generic import (
    ListView,
    DetailView,
    TemplateView,
    View,
    FormView,
)
from django.shortcuts import get_object_or_404, render, redirect
from django.http import JsonResponse

from django.urls import reverse

from bobvance.base.forms import CustomerForm


class Home(TemplateView):
    template_name = "base/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["products"] = Product.objects.order_by("?")[:5]
        return context


class ProductsView(ListView):
    model = Product
    template_name = "base/products.html"
    context_object_name = "products"


class NewProductsView(ListView):
    model = Product
    template_name = "base/products.html"
    context_object_name = "products"

    def get_queryset(self):
        return Product.objects.filter(new=True)


class UsedProductsView(ListView):
    model = Product
    template_name = "base/products.html"
    context_object_name = "products"

    def get_queryset(self):
        return Product.objects.filter(new=False)


class ProductDetailView(DetailView):
    model = Product
    template_name = "base/product_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["more_products"] = Product.objects.exclude(
            pk=self.object.pk
        ).order_by("?")[:5]
        return context


class CartView(View):
    def get(self, request, *args, **kwargs):
        cart = request.session.get("cart", {})

        product_ids = [
            pid
            for pid in cart.keys()
            if pid is not None and pid != "null" and pid.isdigit()
        ]

        cart_items = Product.objects.filter(id__in=product_ids)

        total_price = sum(
            [product.price * cart[str(product.id)] for product in cart_items]
        )

        context = {
            "cart_items": [
                {"product": product, "quantity": cart[str(product.id)]}
                for product in cart_items
            ],
            "total_price": total_price,
        }

        return render(request, "base/cart.html", context)


class AddToCartView(View):
    def post(self, request, *args, **kwargs):
        product_id = request.POST.get("product_id")
        quantity = int(request.POST.get("quantity", 1))

        cart = request.session.get("cart", {})
        if product_id in cart:
            cart[product_id] += quantity
        else:
            cart[product_id] = quantity

        request.session["cart"] = cart

        return redirect("cart")


class UpdateCartView(View):
    def post(self, request, *args, **kwargs):
        product_id = request.POST.get("product_id")
        quantity = int(request.POST.get("quantity"))

        cart = request.session.get("cart", {})
        if product_id in cart and quantity > 0:
            cart[product_id] = quantity
        elif product_id in cart and quantity <= 0:
            del cart[product_id]

        request.session["cart"] = cart

        return redirect("cart")


class RemoveFromCartView(View):
    def post(self, request, *args, **kwargs):
        product_id = request.POST.get("product_id")
        cart = request.session.get("cart", {})

        if product_id in cart:
            del cart[product_id]
            request.session["cart"] = cart
            status = "success"
            message = "Product successfully removed from cart."
        else:
            status = "failed"
            message = "Product not found in cart."

        if request.is_ajax():
            return JsonResponse({"status": status, "message": message})

        return redirect("cart")


class OrderView(FormView):
    form_class = CustomerForm
    template_name = "base/order.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart = self.request.session.get("cart", {})
        product_ids = [
            pid
            for pid in cart.keys()
            if pid is not None and pid != "null" and pid.isdigit()
        ]
        cart_items = Product.objects.filter(id__in=product_ids)
        total_price = sum(
            [product.price * cart[str(product.id)] for product in cart_items]
        )
        context["cart_items"] = [
            {"product": product, "quantity": cart[str(product.id)]}
            for product in cart_items
        ]
        context["total_price"] = total_price
        return context

    def form_valid(self, form):
        cart = self.request.session.get("cart", {})
        product_ids = [
            pid
            for pid in cart.keys()
            if pid is not None and pid != "null" and pid.isdigit()
        ]
        cart_items = Product.objects.filter(id__in=product_ids)
        total_price = sum(
            [product.price * cart[str(product.id)] for product in cart_items]
        )

        customer = form.save()
        order = Order.objects.create(
            customer=customer, total_price=total_price
        )

        for product in cart_items:
            OrderProduct.objects.create(
                order=order, product=product, quantity=cart[str(product.id)]
            )

        del self.request.session["cart"]

        self.object = order

        return super().form_valid(form)

    def get_success_url(self):
        return reverse("success", kwargs={"pk": self.object.pk})


class SuccessView(TemplateView):
    template_name = "base/success.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["order"] = get_object_or_404(Order, pk=self.kwargs["pk"])
        context["orderproduct"] = OrderProduct.objects.filter(
            order=context["order"]
        )
        return context


class AboutUsView(TemplateView):
    template_name = "base/aboutus.html"
