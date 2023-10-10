from django.urls import path, include
from bobvance.base.views import Home, ProductsView, ProductDetailView, AddToCartView, CartView, UpdateCartView, RemoveFromCartView, AboutUsView, NewProductsView, UsedProductsView

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('products/', ProductsView.as_view(), name='products'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('add-to-cart/', AddToCartView.as_view(), name='add_to_cart'),
    path('cart/', CartView.as_view(), name='cart'),
    path('update-cart/', UpdateCartView.as_view(), name='update_cart'),
    path('remove-from-cart/', RemoveFromCartView.as_view(), name='remove_from_cart'),
    path('about-us/', AboutUsView.as_view(), name='about_us'),

    path('products/new/', NewProductsView.as_view(), name='new_products'),
    path('products/used/', UsedProductsView.as_view(), name='used_products'),
]
