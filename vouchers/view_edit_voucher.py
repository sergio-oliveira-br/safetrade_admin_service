from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect

from vouchers.forms import VoucherForm


def _get_vouchers_context(form=None, success=None, error=None):
    """Helper to avoid code repetition in the context"""
    return {
        'form': form or VoucherForm(),
        'success_message': success,
        'error_message': error,
    }

def edit_voucher_page(request):
    return render(request, 'core/edit_voucher.html', _get_vouchers_context(form=VoucherForm(), success=False, error=None))
