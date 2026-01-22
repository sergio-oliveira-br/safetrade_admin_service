from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect

def index_page(request):
    return render(request, 'core/admin.html')
