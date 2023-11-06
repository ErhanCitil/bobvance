from django.urls import reverse

from django_webtest import WebTest

from bobvance.contact.models import Contact
from bobvance.contact.tests.factories import ContactFactory


class ContactViewTest(WebTest):
    def setUp(self):
        self.contact = ContactFactory(
            name="Bob Vance",
            email="bobvance@gmail.com",
            message="I want to buy a",
        )

    def test_contact_view(self):
        response = self.app.get(reverse("contact"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "contact/contact.html")
