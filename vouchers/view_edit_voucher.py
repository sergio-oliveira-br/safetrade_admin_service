from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect

def edit_voucher_page(request):
    return render(request, 'core/edit_voucher.html')
