# vouchers/urls.py

from django.urls import path
from . import view_admin

urlpatterns = [
    path('', view_admin.index_page, name='admin'),
]