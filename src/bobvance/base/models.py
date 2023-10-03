from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from address.models import AddressField

# Create your models here.
class Customer(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField()
    phonenumber = PhoneNumberField()
    address = AddressField(on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"
    