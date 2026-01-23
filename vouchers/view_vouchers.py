from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect

def vouchers_page(request):
    return render(request, 'core/vouchers.html')
