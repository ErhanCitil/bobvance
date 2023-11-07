from django.db import models
from django.utils.translation import gettext_lazy as _


class OrderStatusChoices(models.TextChoices):
    in_progress = "In_progress", _("In progress")
    shipped = "Shipped", _("Shipped")
    delivered = "Delivered", _("Delivered")
    cancelled = "Cancelled", _("Cancelled")
