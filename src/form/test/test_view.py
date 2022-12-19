from django.test import TestCase
from ..models import *
from ..forms import *
from django.urls import reverse
class TestView(TestCase):
    def test_contact(self):
        response = self.client.get('contact')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact.html')
    
    def test_contact_form_input(self):
        form = ContactForm(data={
            'name': 'test',
            'email': 'erhan@live.nl',
            'message': 'Dit is een test bericht!',
        })
        self.assertTrue(form.is_valid())
