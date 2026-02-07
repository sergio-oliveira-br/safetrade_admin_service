from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect

from vouchers.forms import VoucherForm



def edit_voucher_page(request):
    return render(request, 'core/edit_voucher.html', _get_vouchers_context(form=VoucherForm(), success=False, error=None))
