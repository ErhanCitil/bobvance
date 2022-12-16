from django.test import TestCase
from webshop.views import *
from webshop.models import *
from django.urls import reverse

class TestViews(TestCase):
    def setUp(self):
            self.product = Product.objects.create(
            name='test',
            description='Dit is een test beschrijving!',
            price=500.00,
            image='images/1.jpg',
            new = True,
        )

    def test_index(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'webshop/index.html')
    
    def test_assortiment(self):
        response = self.client.get('/assortiment')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'webshop/assortiment.html')

    def test_product(self):
        url = reverse('product', kwargs={'pk': self.product.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('webshop/product.html')