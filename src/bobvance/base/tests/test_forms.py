from bobvance.base.tests.factories import CustomerFactory, ProductFactory
from django_webtest import WebTest
from django.urls import reverse

class FormTestCase(WebTest):
    def setUp(self):
        self.customer = CustomerFactory()
        self.product = ProductFactory()

        self.url = reverse("order")

    def test_order_form_page(self):
        response = self.app.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "base/order.html")

    def test_order_view(self):
        form = self.app.get(self.url).form
        form["firstname"] = self.customer.firstname
        form["lastname"] = self.customer.lastname
        form["email"] = self.customer.email
        form["address"] = self.customer.address
        form["postal_code"] = self.customer.postal_code
        form["city"] = self.customer.city
        form["country"] = self.customer.country
        form["phonenumber"] = str(self.customer.phonenumber)
        form["postal_code"] = self.customer.postal_code
        response = form.submit()
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("success", kwargs={"pk": 1}))

    def test_wrong_phone_number(self):
        """
        The form is only accepting Dutch phone numbers
        """

        form = self.app.get(self.url).form
        form["phonenumber"] =  "1234567890"
        response = form.submit()
        self.assertEqual(response.context["form"].errors['phonenumber'][0], 'Het ingevoerde telefoonnummer is niet juist. Gebruik het formaat +31 6xxxxxxxx.')

    def test_wrong_postal_code(self):
        """
        The form is only accepting Dutch postal codes
        """

        form = self.app.get(self.url).form
        form["postal_code"] =  "1234ABB"
        response = form.submit()
        self.assertEqual(response.context["form"].errors['postal_code'][0], 'Enter a valid zip code.')

    def test_wrong_email(self):
        form = self.app.get(self.url).form
        form["email"] =  "test"
        response = form.submit()
        self.assertEqual(response.context["form"].errors['email'][0], 'Voer een geldig e-mailadres in.')

    def test_empty_form(self):
        form = self.app.get(self.url).form
        response = form.submit()
        self.assertEqual(response.context["form"].errors['firstname'][0], 'Dit veld is verplicht.')
        self.assertEqual(response.context["form"].errors['lastname'][0], 'Dit veld is verplicht.')
        self.assertEqual(response.context["form"].errors['email'][0], 'Dit veld is verplicht.')
        self.assertEqual(response.context["form"].errors['address'][0], 'Dit veld is verplicht.')
        self.assertEqual(response.context["form"].errors['postal_code'][0], 'Dit veld is verplicht.')
        self.assertEqual(response.context["form"].errors['city'][0], 'Dit veld is verplicht.')
        self.assertEqual(response.context["form"].errors['country'][0], 'Dit veld is verplicht.')
        self.assertEqual(response.context["form"].errors['phonenumber'][0], 'Dit veld is verplicht.')
