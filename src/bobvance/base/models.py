from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from localflavor.nl.models import NLZipCodeField

from django.core.validators import MinValueValidator

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

class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='product_img/')
    new = models.BooleanField(default=True)

    def __str__(self):
        return self.name

IN_PROGRESS = 'In_progress'
SHIPPED = 'Shipped'
DELIVERED = 'Delivered'
CANCELLED = 'Cancelled'

ORDER_STATUS_CHOICES = (
    (IN_PROGRESS, 'In progress'),
    (SHIPPED, 'Shipped'),
    (DELIVERED, 'Delivered'),
    (CANCELLED, 'Cancelled'),
)

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, choices=ORDER_STATUS_CHOICES, default=ORDER_STATUS_CHOICES[0][0])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.customer} - {self.status}"

class OrderProduct(models.Model):
    order = models.ForeignKey(Order, related_name='order_products',on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_products', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1)])

    def __str__(self):
        return f"{self.product.name} - {self.quantity}x"

    class Meta:
        unique_together = ['order', 'product']
        ordering = ['order']
