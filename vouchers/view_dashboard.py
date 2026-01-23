from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect

def dashboard_page(request):
    return render(request, 'core/dashboard.html')
