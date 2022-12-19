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
    new = models.BooleanField(default=True)

    def __str__(self):
        return self.name

ORDER_STATUS_CHOICES = (
    # Nooit handig om spaties en hoofdlettergevoeligheid te gebruiken voor database waarden
    ('in_behandeling', 'In behandeling'),
    ('verzonden', 'Verzonden'),
    ('afgeleverd', 'Afgeleverd'),
    ('geannuleerd', 'Geannuleerd'),
)

class Cart(models.Model):
    # Created_at is voor later, omdat ik ook dingen wil doen met de custom management command
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Cart {self.id}"

class CartProduct(models.Model):
    cart = models.ForeignKey(Cart, related_name="cart_product", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name="cart_product", on_delete=models.CASCADE)
    
    def __str__(self):
        return f"Cart {self.cart.id}"

class Order(models.Model):
    customer = models.ForeignKey(Customer, related_name="orders",on_delete=models.CASCADE)
    status = models.CharField(max_length=100, choices=ORDER_STATUS_CHOICES, default='In behandeling')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Order {self.id}"

class OrderProduct(models.Model):
    order = models.ForeignKey(Order, related_name="order_product", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name="order_product", on_delete=models.CASCADE)
    amount = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"Order {self.order.id}"
    # inline model in django admin

class Verzekering(models.Model):
    name = models.CharField(max_length=100)
    product = models.ManyToManyField(Product, related_name='verzekeringen')

    def __str__(self):
        return self.name

