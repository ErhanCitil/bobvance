from django.contrib import admin

from bobvance.base.models import Customer, Product, OrderProduct, Order

# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("firstname", "lastname", "email")
admin.site.register(Customer, CustomerAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "new")
admin.site.register(Product, ProductAdmin)

admin.site.register(OrderProduct)
class OrderProductInline(admin.TabularInline):
    model = OrderProduct
    extra = 0

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderProductInline]
