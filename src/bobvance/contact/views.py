from django.shortcuts import render
from django.views.generic import FormView

from bobvance.contact.forms import ContactForm

# Create your views here.


class ContactView(FormView):
    template_name = "contact/contact.html"
    form_class = ContactForm
    success_url = "/contact/"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
