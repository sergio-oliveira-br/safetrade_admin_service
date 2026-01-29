# vouchers/view_vouchers.py

from botocore.exceptions import ClientError
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods

from vouchers.forms import VoucherForm
from vouchers.model_voucher import Voucher


def vouchers_page(request):
    form = VoucherForm(request.POST or None)

    voucher_list = Voucher.list_vouchers_by_status('Active')

    context = {
        'voucher_table': voucher_list,
        'form': form,
    }

    return render(request, 'core/vouchers.html', context)


@require_http_methods(['GET', 'POST'])
def create_voucher(request):

    form = VoucherForm(request.POST or None)
    success_message = None
    error_message = None

    if request.method == 'POST' and form.is_valid():

        data = form.cleaned_data

        try:
            voucher = Voucher(
                voucher_description=data['voucher_description'],
                voucher_status=data['voucher_status'],
                voucher_price=data['voucher_price'],
                voucher_quantity=data['voucher_quantity']
            )

            # voucher.save()
            voucher.save_multiple_vouchers()
            success_message = 'The voucher creation process has been completed successfully.'

            form = VoucherForm()

        except ClientError as e:
            error_message = str(e)

        except Exception as e:
            error_message = 'Sorry, something went wrong'

    elif request.method == 'POST':
        error_message = 'Please check your input data and try again'

    context = {
        'form': form,
        'success_message': success_message,
        'error_message': error_message,
    }

    return render(request, 'core/vouchers.html', context)