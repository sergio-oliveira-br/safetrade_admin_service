from django.contrib import messages
from django.shortcuts import render

def delete_voucher_page(request, voucher_id):
    context = {
        'voucher_id': voucher_id,
    }
    return render(request,'core/delete_voucher.html', context )