from django.contrib import messages
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect

from vouchers.forms import VoucherForm
from vouchers.model_voucher import Voucher


def edit_voucher_page(request, voucher_id):
    voucher_data = Voucher.find_voucher_by_id(voucher_id)
    form = VoucherForm(initial=voucher_data)

    # if user submit the form
    if request.method == 'POST':

        form_updated = VoucherForm(request.POST)
        if form_updated.is_valid():
            Voucher.edit_voucher(form_updated.cleaned_data, voucher_id)
            messages.success(request, f"Voucher {voucher_id} updated successfully")

        else:
            messages.error(request, f"Form was not valid! Voucher ID: {voucher_id} not edited")

    context = {
        'voucher_id': voucher_id,
        'form': form,
    }
    return render(request,'core/edit_voucher.html', context)
