from django.db import models
from django.core.validators import MinValueValidator
from localflavor.nl.models import NLZipCodeField
from phonenumber_field.modelfields import PhoneNumberField
from bobvance.base.choices import OrderStatusChoices, PaymentMethodChoices, PaymentStatusChoices

class Customer(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField()
    phonenumber = PhoneNumberField(error_messages={"invalid": "Het ingevoerde telefoonnummer is niet juist. Gebruik het formaat +31 6xxxxxxxx."})
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
    image = models.ImageField(upload_to="product_img/")
    new = models.BooleanField(default=True)
    review = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Payment(models.Model):
    method = models.CharField(max_length=50, choices=PaymentMethodChoices.choices, default=PaymentMethodChoices.credit_card)
    status = models.CharField(max_length=20, choices=PaymentStatusChoices.choices, default=PaymentStatusChoices.pending)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.method} - {self.status}"


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    payment = models.ForeignKey(Payment, on_delete=models.SET_NULL, null=True, blank=True)
    status = models.CharField(
        max_length=50,
        choices=OrderStatusChoices.choices,
        default=OrderStatusChoices.in_progress,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=5, decimal_places=0, default=0)

    def __str__(self):
        return f"{self.customer} - {self.id}"


class OrderProduct(models.Model):
    order = models.ForeignKey(
        Order,
        related_name="order_products",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    product = models.ForeignKey(
        Product, related_name="product_orders", on_delete=models.CASCADE
    )
    quantity = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1)])

    def __str__(self):
        return f"{self.product.name} - {self.quantity}x"

    def total_price(self):
        return self.product.price * self.quantity

    class Meta:
        unique_together = ("order", "product")
        ordering = ["order"]
