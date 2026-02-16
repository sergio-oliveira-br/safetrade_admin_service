# vouchers/view_vouchers.py
from django.core.paginator import Paginator
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from vouchers.forms.form_for_creation import VoucherCreationForm
from vouchers.model_voucher import Voucher
from vouchers.services.voucher_admin_service import VoucherAdminService


def _get_vouchers_context(request, form=None, success=None, error=None):
    """Helper to avoid code repetition in the context"""

    all_vouchers = Voucher.list_all_vouchers()
    number_of_vouchers = len(all_vouchers)

    paginator = Paginator(all_vouchers, 10)
    num_pages = request.GET.get('page')
    page_obj = paginator.get_page(num_pages)


    return {
        'number_of_vouchers': number_of_vouchers,
        'page_obj': page_obj,
        'form': form or VoucherCreationForm(),
        'success_message': success,
        'error_message': error,
    }

def vouchers_page(request):
    context = _get_vouchers_context(request)
    return render(request, 'core/pages/vouchers.html', context)


@require_http_methods(['POST'])
def create_voucher(request):

    form = VoucherCreationForm(request.POST or None)
    success_message = None
    error_message = None

    if not form.is_valid():
        error_message = 'Please check your input data and try again.'

    elif form.is_valid():
        service = VoucherAdminService()
        result = service.register_new_vouchers(form.cleaned_data)

        if result['success']:
            success_message = result['message']
            form = VoucherCreationForm()

        else:
            error_message = result['message']

    return render(request,
                  'core/pages/vouchers.html',
                  _get_vouchers_context(form, success_message, error_message))