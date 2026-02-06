# vouchers/view_vouchers.py

from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from vouchers.forms import VoucherForm
from vouchers.model_voucher import Voucher
from vouchers.services.voucher_admin_service import VoucherAdminService


def _get_vouchers_context(form=None, success=None, error=None):
    """Helper to avoid code repetition in the context"""
    return {
        'voucher_table': Voucher.list_vouchers_by_status(),
        'form': form or VoucherForm(),
        'success_message': success,
        'error_message': error,
    }

def vouchers_page(request):
    return render(request,'core/vouchers.html',_get_vouchers_context())


@require_http_methods(['POST'])
def create_voucher(request):

    form = VoucherForm(request.POST or None)
    success_message = None
    error_message = None

    if not form.is_valid():
        error_message = 'Please check your input data and try again.'

    elif form.is_valid():
        service = VoucherAdminService()
        result = service.register_new_vouchers(form.cleaned_data)

        if result['success']:
            success_message = result['message']
            form = VoucherForm()

        else:
            error_message = result['message']

    return render(request,
                  'core/vouchers.html',
                  _get_vouchers_context(form, success_message, error_message))