from django.contrib import messages
from django.shortcuts import render

from vouchers.model_voucher import Voucher


def delete_voucher_page(request, voucher_id):

    voucher = Voucher.find_voucher_by_id(voucher_id)

    context = {
        'voucher': voucher,
        'voucher_id': voucher_id,
    }
    return render(request,'core/delete_voucher.html', context )