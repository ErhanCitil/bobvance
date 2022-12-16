from django.urls import path

from .views import *

urlpatterns = [
    path('contact/', ContactSite.as_view(), name='contact')
]