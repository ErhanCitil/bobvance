from django.test import TestCase
from django.urls import reverse

from bobvance.base.tests.factories import CustomerFactory, ProductFactory


class ViewsTestCase(TestCase):
    def home_view(self):
        url = reverse("home")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def products_view(self):
        url = reverse("products")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def new_products_view(self):
        url = reverse("new_products")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def used_products_view(self):
        url = reverse("used_products")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def product_detail_view(self):
        product = ProductFactory()
        url = reverse("product_detail", kwargs={"pk": product.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def cart_view(self):
        url = reverse("cart")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def checkout_view(self):
        url = reverse("checkout")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def order_view(self):
        url = reverse("order")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)


class NewAndUsedProductsTestCase(TestCase):
    def setUp(self):
        self.new_product = ProductFactory(new=True)
        self.used_product = ProductFactory(new=False)

    def test_new_products_view(self):
        url = reverse("new_products")
        response = self.client.get(url)
        self.assertContains(response, self.new_product.name)
        self.assertNotContains(response, self.used_product.name)

    def test_used_products_view(self):
        url = reverse("used_products")
        response = self.client.get(url)
        self.assertContains(response, self.used_product.name)
        self.assertNotContains(response, self.new_product.name)


class ProductDetailViewTestCase(TestCase):
    def setUp(self):
        self.product = ProductFactory()
        self.url = reverse("product_detail", kwargs={"pk": self.product.pk})

    def test_product_detail_view(self):
        response = self.client.get(self.url)
        self.assertContains(response, self.product.name)
        self.assertContains(response, self.product.description)

    def test_product_detail_view_more_products(self):
        product_1 = ProductFactory()
        product_2 = ProductFactory()
        product_3 = ProductFactory()
        product_4 = ProductFactory()
        product_5 = ProductFactory()
        response = self.client.get(self.url)
        self.assertContains(response, product_1.name)
        self.assertContains(response, product_2.name)
        self.assertContains(response, product_3.name)
        self.assertContains(response, product_4.name)
        self.assertContains(response, product_5.name)
