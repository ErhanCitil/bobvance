from django.urls import path, include
from bobvance.base.views import Home, ProductsView, ProductDetailView

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('products/', ProductsView.as_view(), name='products'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
]
