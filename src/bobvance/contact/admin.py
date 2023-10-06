from django.contrib import admin
from bobvance.contact.models import Contact
# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "created_at")

admin.site.register(Contact, ContactAdmin)
