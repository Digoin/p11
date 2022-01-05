from django.shortcuts import render
from main_site.models import Product
import string

# Create your views here.

def home(request):
    return render(request, 'main_site/welcome_page.html')

def legal_notice(request):
    return render(request, 'main_site/legal_notice.html')
  
def product_description(request, product_id):
    substitute_products = []
    best_subsitute_products = []
    nutriscore_count = 0
    product = Product.objects.get(id=product_id)
    for categories in product.category_set.all():
        for linked_product in categories.products.all():
            if string.ascii_uppercase.index(linked_product.nutriscore) <= string.ascii_uppercase.index(product.nutriscore) and linked_product not in substitute_products and linked_product != product:
                substitute_products.append(linked_product)
    while nutriscore_count < 4:
        for best_product in substitute_products:
            if len(best_subsitute_products) >= 6:
                break
            if string.ascii_uppercase.index(best_product.nutriscore) == nutriscore_count:
                best_subsitute_products.append(best_product)
        nutriscore_count += 1
    context = {
        "product_name" : product.name,
        "product_nutriscore" : product.nutriscore,
        "product_url" : product.url,
        "product_image" : product.img_url,
        "substitute_products" : best_subsitute_products,
    }
    return render(request, 'main_site/product_description_page.html', context)