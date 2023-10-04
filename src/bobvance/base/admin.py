from django.contrib import admin

from bobvance.base.models import Customer, Product, OrderProduct, Order

# Register your models here.
admin.site.register(Customer)
admin.site.register(Product)

admin.site.register(OrderProduct)
class OrderProductInline(admin.TabularInline):
    model = OrderProduct
    extra = 1

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderProductInline]
