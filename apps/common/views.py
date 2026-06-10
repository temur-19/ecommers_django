from django.shortcuts import render
from apps.products.models import Product
# Create your views here.

def home(request):
    product  = Product.objects.all()
    return render(request, 'common/home.html', {'product':product})

