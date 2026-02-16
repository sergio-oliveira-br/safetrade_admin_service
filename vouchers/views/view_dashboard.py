from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect

from vouchers.model_voucher import Voucher


def dashboard_page(request):

    active_count = Voucher.count_vouches_by_status('Active')
    pending_count = Voucher.count_vouches_by_status('Pending')
    sold_count = Voucher.count_vouches_by_status('Sold')
    gifted_count = Voucher.count_vouches_by_status('Gifted')

    context = {
        'active_count': active_count,
        'pending_count': pending_count,
        'sold_count': sold_count,
        'gifted_count': gifted_count,
    }

    return render(request, 'core/pages/dashboard.html', context)

def voucher_by_status_page(request, voucher_status):
    service_response = Voucher.list_vouchers_by_status(voucher_status)
    return render(request, 'core/pages/../templates/core/componenets/dash_table.html', context={'voucher_table': service_response})
