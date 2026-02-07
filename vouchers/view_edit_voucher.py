from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect

from vouchers.forms import VoucherForm
from vouchers.model_voucher import Voucher


def edit_voucher_page(request, voucher_id):
    voucher_data = Voucher.find_voucher_by_id(voucher_id)
    form = VoucherForm(initial=voucher_data)

    context = {
        'form': form,
    }
    return render(request,'core/edit_voucher.html', context)
