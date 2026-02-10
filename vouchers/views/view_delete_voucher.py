from django.contrib import messages
from django.shortcuts import render, redirect

from vouchers.model_voucher import Voucher


def delete_voucher_page(request, voucher_id):

    voucher = Voucher.find_voucher_by_id(voucher_id)

    context = {
        'voucher': voucher,
        'voucher_id': voucher_id,
    }
    return render(request, 'core/delete_voucher.html', context)

def delete_voucher(request, voucher_id):

    voucher = Voucher.find_voucher_by_id(voucher_id)

    if not voucher:
        messages.error(request, f"Voucher {voucher_id} not found")

    # Invoke the service method to delete the item from DB
    delete_service = Voucher.delete_voucher(voucher_id)

    if not delete_service['success']:
        messages.error(request, delete_service['message'])
        return redirect('vouchers')

    messages.success(request, f"Voucher ID: {voucher_id} deleted successfully")
    return redirect('vouchers')