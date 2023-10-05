from django.urls import path, include
from bobvance.base.views import Home, ProductsView

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('products/', ProductsView.as_view(), name='products'),
]
