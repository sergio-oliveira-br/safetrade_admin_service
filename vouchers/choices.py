# vouchers/choices.py

from django.db import models

class VoucherStatus(models.TextChoices):
    ACTIVE = 'Active', 'Active'
    SOLD = 'Sold', 'Sold'
    PENDING = 'Pending', 'Pending'