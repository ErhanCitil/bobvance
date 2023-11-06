from django import forms
from django.contrib import admin
from django.db import models

from bobvance.base.models import Customer, Order, OrderProduct, Product

# Register your models here.


class CustomerAdmin(admin.ModelAdmin):
    list_display = ("firstname", "lastname", "email")


admin.site.register(Customer, CustomerAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "new")


admin.site.register(Product, ProductAdmin)


class ReadOnlyTabularInline(admin.TabularInline):
    model = OrderProduct
    extra = 0

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        kwargs["disabled"] = True
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    def formfield_for_dbfield(self, db_field, request, **kwargs):
        if isinstance(db_field, (models.CharField, models.TextField)):
            kwargs["widget"] = forms.TextInput(attrs={"readonly": "readonly"})
        elif isinstance(db_field, models.BooleanField):
            kwargs["widget"] = forms.CheckboxInput(attrs={"disabled": "readonly"})
        else:
            kwargs["widget"] = forms.TextInput(attrs={"disabled": "readonly"})
        return super().formfield_for_dbfield(db_field, request, **kwargs)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ["customer", "status", "created_at", "total_price"]
    inlines = [ReadOnlyTabularInline]
    readonly_fields = ["customer", "total_price"]
