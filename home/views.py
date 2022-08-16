from django.shortcuts import render
from products.models import Product


def index(request):
    """ A view to return the index page and sort products by ids"""
    products = Product.objects.all().order_by('-id')
    return render(request, 'home/index.html', {'products': products})
