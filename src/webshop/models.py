from django.db import models

# Create your models here.
class Customer(models.Model):
    naam = models.CharField(max_length=100)
    achternaam = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    telefoonnummer = models.CharField(max_length=100)
    adres = models.CharField(max_length=100)
    postcode = models.CharField(max_length=100)
    plaats = models.CharField(max_length=100)
    land = models.CharField(max_length=100)
    
    def __str__(self):
        return self.naam

class Product(models.Model):
    naam = models.CharField(max_length=100)
    prijs = models.FloatField()
    beschrijving = models.CharField(max_length=1000)
    afbeelding = models.ImageField(upload_to='images/')
    customer = models.ManyToManyField(Customer, related_name="producten", through='Order')
    nieuw = models.BooleanField(default=True)

    def __str__(self):
        return self.naam

class Order(models.Model):
    customer = models.ForeignKey(Customer, related_name="orders",on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name="orders", on_delete=models.CASCADE)
    aantal = models.IntegerField()
    datum = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.order.id

class Verzekering(models.Model):
    naam = models.CharField(max_length=100)
    product = models.ManyToManyField(Product, related_name='verzekeringen')

    def __str__(self):
        return self.naam