# vouchers/urls.py

from django.urls import path
from . import view_vouchers, view_dashboard, view_index, view_edit_voucher

urlpatterns = [
    # Index
    path('', view_index.index_page, name='index'),

    # Admin
    path('vouchers/', view_vouchers.vouchers_page, name='vouchers'),
    path('vouchers/create', view_vouchers.create_voucher, name='create_voucher'),

    # Dashboard
    path('dashboard/', view_dashboard.dashboard_page, name='dashboard'),
    path('edit/', view_edit_voucher.edit_voucher_page, name='edit_page'),

]