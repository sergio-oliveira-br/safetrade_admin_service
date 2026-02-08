# vouchers/forms/form_for_creation.py
from django import forms
from vouchers.forms.form_base import VoucherBaseForm


class VoucherCreationForm(VoucherBaseForm):
    voucher_quantity = forms.IntegerField(
        label='Voucher Quantity',
        min_value=1,
        max_value=5,
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
