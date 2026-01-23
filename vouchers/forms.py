# vouchers/forms.py

from django import forms
from .choices import CountryCode, VoucherStatus

class VoucherForm(forms.Form):
    voucher_description = forms.CharField(
        label='Voucher Description',
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    voucher_price = forms.DecimalField(
        label='Voucher Price',
        min_value=1,
        max_digits=10,
        decimal_places=2,
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )

    voucher_quantity = forms.IntegerField(
        label='Voucher Quantity',
        min_value=1,
        max_value=20,
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )

    voucher_location = forms.ChoiceField(
        label='Voucher Location',
        choices=CountryCode.choices,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    voucher_status = forms.ChoiceField(
        label='Voucher Status',
        choices=VoucherStatus.choices,
        widget=forms.Select(attrs={'class': 'form-control'})
    )