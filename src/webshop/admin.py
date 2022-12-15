from django.contrib import admin
from .models import *
# Register your models here.
class OrderInline(admin.TabularInline):
    model = OrderProduct

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderInline]

for model in [Customer, Verzekering]:
    admin.site.register(model)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'new', 'price' )
    list_filter = ('new', )