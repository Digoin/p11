from django.shortcuts import render
from main_site.models import Product

# Create your views here.

def home(request):
    return render(request, 'main_site/welcome_page.html')

def legal_notice(request):
    return render(request, 'base/legal_notice.html')

def product_description(request, product_id):
    product = Product.objects.get(id=product_id)
    context = {
        "product_name" : product.name,
        "product_nutriscore" : product.nutriscore,
    }
    return render(request, 'main_site/product_description_page.html', context)