import factory
from factory.fuzzy import FuzzyChoice
from bobvance.base.models import Customer, Order, OrderProduct, Product
import random

class CustomerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Customer

    firstname = factory.Faker("first_name")
    lastname = factory.Faker("last_name")
    email = factory.Faker("email")
    phonenumber = factory.LazyFunction(lambda: f"+31 6{random.randint(100, 999)}{random.randint(10000, 99999)}")
    address = factory.Faker("street_address")
    postal_code = factory.LazyFunction(lambda: f"{random.randint(1000, 9999)} {''.join(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ') for i in range(2))}")
    city = factory.Faker("city")
    country = factory.Faker("country")

class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product

    name = factory.Faker("word")
    price = factory.Faker("pydecimal", left_digits=3, right_digits=2, positive=True)
    description = factory.Faker("text")
    image = factory.django.ImageField(color="blue")
    new = FuzzyChoice([True, False])
