from .views import *
from django.urls import path

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('product/<int:pk>', ProductSite.as_view(), name='product'),
    path('assortiment', Assortiment.as_view(), name='assortiment'),
]