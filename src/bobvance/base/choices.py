from django.db import models
from django.utils.translation import gettext_lazy as _


class OrderStatusChoices(models.TextChoices):
    in_progress = "In_progress", _("In progress")
    shipped = "Shipped", _("Shipped")
    delivered = "Delivered", _("Delivered")
    cancelled = "Cancelled", _("Cancelled")

class PaymentMethodChoices(models.TextChoices):
    credit_card = 'credit_card', _('Credit Card')
    debit_card = 'debit_card', _('Debit Card')
    paypal = 'paypal', _('PayPal')
    bank_transfer = 'bank_transfer', _('Bank Transfer')
    cash = 'cash', _('Cash')

class PaymentStatusChoices(models.TextChoices):
    pending = "Pending", _("Pending")
    completed = "Completed", _("Completed")
    failed = "Failed", _("Failed")
