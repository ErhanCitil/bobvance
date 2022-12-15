from django.contrib import admin
from .models import *
# Register your models here.
for i in [Customer, Product, Order, Verzekering]:
    admin.site.register(i)