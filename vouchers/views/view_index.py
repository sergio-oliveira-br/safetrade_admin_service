from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views.decorators.http import require_GET


@require_GET
def index_page(request):
    return render(request, 'core/pages/index.html')
