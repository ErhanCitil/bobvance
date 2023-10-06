from bobvance.contact.models import Contact
from django.test import TestCase
from bobvance.contact.tests.factories import ContactFactory

class ContactModelTest(TestCase):
    def setUp(self):
        self.contact = ContactFactory(
            name='Bob Vance',
            email='bobvance@gmail.com',
            message="I want to buy a"
        )

    def test_contact_model(self):
        self.assertEqual(self.contact.name, 'Bob Vance')
        self.assertEqual(self.contact.email, 'bobvance@gmail.com')
        self.assertEqual(self.contact.message, 'I want to buy a')
        self.assertEqual(self.contact.created_at, self.contact.created_at)

    def test_contact_str(self):
        self.assertEqual(str(self.contact), 'Bob Vance')

    def test_contact_verbose_name_plural(self):
        self.assertEqual(str(Contact._meta.verbose_name_plural), 'contacts')

    def test_contact_verbose_name(self):
        self.assertEqual(str(Contact._meta.verbose_name), 'contact')
        