# vouchers/choices.py

from django.db import models

class CountryCode(models.TextChoices):
    BRAZIL = 'BR', 'Brazil'
    IRELAND = 'IE', 'Ireland'
    PORTUGAL = 'PT', 'Portugal'
    UK = 'UK', 'United Kingdom'

class VoucherStatus(models.TextChoices):
    ACTIVE = 'Active', 'Active'
    INACTIVE = 'Inactive', 'Inactive'
    PENDING = 'Pending', 'Pending'