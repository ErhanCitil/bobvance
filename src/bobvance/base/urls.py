from django.urls import path, include
from bobvance.base.views import Home, ProductsView, ProductDetailView, CartView, AddToCartView

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('products/', ProductsView.as_view(), name='products'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('cart/', CartView.as_view(), name='cart'),
    path('add_to_cart/', AddToCartView.as_view(), name='add_to_cart'),
]
