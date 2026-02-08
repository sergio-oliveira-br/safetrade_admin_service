# vouchers/forms/form_for_edition.py
from django import forms

from vouchers.forms.form_base import VoucherBaseForm


class VoucherEditionForm(VoucherBaseForm):
    voucher_tx_hash = forms.CharField(
        label='Voucher Tx Hash',
        min_length=1,
        max_length=50,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )