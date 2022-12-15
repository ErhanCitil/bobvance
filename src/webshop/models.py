from django.db import models

# Create your models here.
class Customer(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phonenumber = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    postcode = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    
    def __str__(self):
        return self.firstname

class Product(models.Model):
    name = models.CharField(max_length=100)
    # Prijzen een DecimalField voor gebruiken
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    # Alles wat meer dan 1 regel bevat gewoon een TextField voor gebruiken
    description = models.TextField(default="")
    image = models.ImageField(upload_to='images/')
    customer = models.ManyToManyField(Customer, related_name="producten", through='Order')
    new = models.BooleanField(default=True)

    def __str__(self):
        return self.name

ORDER_STATUS_CHOICES = (
    ('In behandeling', 'In behandeling'),
    ('Verzonden', 'Verzonden'),
    ('Afgeleverd', 'Afgeleverd'),
    ('Geannuleerd', 'Geannuleerd'),
)

class Order(models.Model):
    customer = models.ForeignKey(Customer, related_name="orders",on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name="orders", on_delete=models.CASCADE)
    # Amount kan niet een negatief getal zijn.
    amount =  models.PositiveIntegerField(default=1)
    status = models.CharField(max_length=100, choices=ORDER_STATUS_CHOICES, default='In behandeling')

    def __str__(self):
        return f"Order {self.id}"

class Verzekering(models.Model):
    name = models.CharField(max_length=100)
    product = models.ManyToManyField(Product, related_name='verzekeringen')

    def __str__(self):
        return self.name

