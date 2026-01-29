# vouchers/choices.py

from django.db import models

class VoucherStatus(models.TextChoices):
    ACTIVE = 'Active', 'Active'
    INACTIVE = 'Inactive', 'Inactive'
    PENDING = 'Pending', 'Pending'