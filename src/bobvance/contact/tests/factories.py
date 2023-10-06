import factory
from bobvance.contact.models import Contact

class ContactFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Contact

    created_at = factory.Faker('date_time')

