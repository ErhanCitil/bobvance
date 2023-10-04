from django.contrib import admin

from bobvance.base.models import Customer, Product, OrderProduct, Order

# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("firstname", "lastname", "email")
admin.site.register(Customer, CustomerAdmin)

admin.site.register(Product)

class OrderProductInline(admin.TabularInline):
    model = OrderProduct
    extra = 1

class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderProductInline]
admin.register(Order, OrderAdmin)
