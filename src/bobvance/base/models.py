from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from localflavor.nl.models import NLZipCodeField

# Create your models here.
class Customer(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField()
    phonenumber = PhoneNumberField()
    address = models.CharField(max_length=100)
    postal_code = NLZipCodeField()
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"
