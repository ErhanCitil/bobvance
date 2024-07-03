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

    def test_contact_form(self):
        form = self.app.get(reverse("contact")).form
        form["name"] = self.contact.name
        form["email"] = self.contact.email
        form["message"] = self.contact.message
        response = form.submit()
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Contact.objects.count(), 2)
        self.assertEqual(Contact.objects.last().name, self.contact.name)
        self.assertEqual(Contact.objects.last().email, self.contact.email)
        self.assertEqual(Contact.objects.last().message, self.contact.message)

    def test_wrong_email(self):
        form = self.app.get(reverse("contact")).form
        form["email"] = "test"
        response = form.submit()
        self.assertEqual(
            response.context["form"].errors["email"][0],
            "Voer een geldig e-mailadres in.",
        )

    def test_empty_name_field(self):
        form = self.app.get(reverse("contact")).form
        form["name"] = ""
        response = form.submit()
        self.assertEqual(
            response.context["form"].errors["name"][0], "Dit veld is verplicht."
        )
