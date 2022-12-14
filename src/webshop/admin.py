from django.contrib import admin
from .models import *
# Register your models here.
for model in [Customer, Product, Order, Verzekering]:
    admin.site.register(model)
