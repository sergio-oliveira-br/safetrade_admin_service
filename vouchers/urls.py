# vouchers/urls.py

from django.urls import path
from .views import view_delete_voucher, view_dashboard, view_edit_voucher, view_index, view_vouchers

urlpatterns = [
    # Index
    path('', view_index.index_page, name='index'),
    # Admin
    path('vouchers/', view_vouchers.vouchers_page, name='vouchers'),
    path('vouchers/create', view_vouchers.create_voucher, name='create_voucher'),

    # Dashboard
    path('dashboard/', view_dashboard.dashboard_page, name='dashboard'),
    path('edit_voucher/<str:voucher_id>/', view_edit_voucher.edit_voucher_page, name='edit_page'),

    path('delete_voucher_page/<str:voucher_id>', view_delete_voucher.delete_voucher_page, name='delete_page'),
    path('delete_voucher/<str:voucher_id>', view_delete_voucher.delete_voucher, name='delete_voucher'),

]