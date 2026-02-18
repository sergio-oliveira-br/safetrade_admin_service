from django.contrib import messages
from django.shortcuts import render
from django.views.decorators.http import require_POST

from vouchers.forms.form_for_edition import VoucherEditionForm
from vouchers.model_voucher import Voucher

def edit_voucher_page(request, voucher_id):
    voucher_data = Voucher.find_voucher_by_id(voucher_id)
    form = VoucherEditionForm(initial=voucher_data)

    # if user submit the form
    if request.method == 'POST':

        form = VoucherEditionForm(request.POST)
        if form.is_valid():
            Voucher.edit_voucher(form.cleaned_data, voucher_id)
            messages.success(request, f"Voucher {voucher_id} updated successfully")

        else:
            messages.error(request, f"Form was not valid! Voucher ID: {voucher_id} not edited")

    return render(request, 'core/pages/edit_voucher.html', {'form': form, 'voucher_id': voucher_id})