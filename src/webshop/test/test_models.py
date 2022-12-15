from django.test import TestCase
from webshop.models import *
import datetime as dt
class TestModels(TestCase):
    def setUp(self):
        self.customer = Customer.objects.create(
                firstname='test',
                lastname='test',
                email = 'test@test.nl',
                phonenumber = '0612345678',
                address = 'teststraat 1',
                postcode = '1099 RR',
                city = 'teststad',
                country = 'testland')
        self.product = Product.objects.create(
            name='test',
            description='Dit is een test beschrijving!',
            price=500.00,
            image='images/1.jpg',
            new = True,
        )

        self.order = Order.objects.create(
            customer=self.customer,
            product=self.product,
            amount=1,
            status='In behandeling',
        )

        self.verzekering = Verzekering.objects.create(
            name='test',
        )

        self.verzekering.product.add(self.product)
        self.verzekering.save()

        self.product.customer.add(self.customer)
        self.product.save()

    def test_product(self):
        self.assertEqual(self.product.name, 'test')
        self.assertEqual(self.product.description, 'Dit is een test beschrijving!')
        self.assertEqual(self.product.price, 500.00)
        self.assertEqual(self.product.image, 'images/1.jpg')
        self.assertEqual(self.product.new, True)
        self.assertEqual(self.product.customer.first(), self.customer)

    def test_customer(self):
        self.assertEqual(self.customer.firstname, 'test')
        self.assertEqual(self.customer.lastname, 'test')
        self.assertEqual(self.customer.email, 'test@test.nl')
        self.assertEqual(self.customer.phonenumber, '0612345678')
        self.assertEqual(self.customer.address, 'teststraat 1')
        self.assertEqual(self.customer.postcode, '1099 RR')
        self.assertEqual(self.customer.city, 'teststad')
        self.assertEqual(self.customer.country, 'testland')

    def test_order(self):
        self.assertEqual(self.order.customer, self.customer)
        self.assertEqual(self.order.product, self.product)
        self.assertEqual(self.order.amount, 1)
        self.assertEqual(self.order.status, 'In behandeling')

    def test_verzekering(self):
        self.assertEqual(self.verzekering.name, 'test')
        self.assertEqual(self.verzekering.product.first(), self.product)