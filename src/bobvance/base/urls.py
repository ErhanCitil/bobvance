from django.urls import path, include
from bobvance.base.views import Home, ProductsView, ProductDetailView, CartView, AddToCartView, RemoveFromCartView, UpdateCartView

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('products/', ProductsView.as_view(), name='products'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('cart/', CartView.as_view(), name='cart'),
    path('add_to_cart/', AddToCartView.as_view(), name='add_to_cart'),
    path('remove-from-cart/', RemoveFromCartView.as_view(), name='remove-from-cart'),
    path('update-cart/', UpdateCartView.as_view(), name='update_cart'),
]
