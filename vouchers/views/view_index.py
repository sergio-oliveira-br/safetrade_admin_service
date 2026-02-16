from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views.decorators.http import require_safe


@require_safe
def index_page(request):
    return render(request, 'core/pages/index.html')
