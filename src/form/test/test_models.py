from django.test import TestCase
from ..models import *

class ContactModelTest(TestCase):
    def setUp(self):
        self.contact = Contact.objects.create(name='Erhan', email='erhan@live.nl', message='Hello World', order_id=1)

    def test_name(self):
        self.assertEqual(self.contact.name, 'Erhan')

    def test_email(self):
        self.assertEqual(self.contact.email, 'erhan@live.nl')

    def test_message(self):
        self.assertEqual(self.contact.message, 'Hello World')

    def test_order_id(self):
        self.assertEqual(self.contact.order_id, 1)