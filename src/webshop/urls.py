from .views import *
from django.urls import path

urlpatterns = [
    path('', Index.as_view(), name='index'),
]