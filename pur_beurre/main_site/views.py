import string
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from main_site.models import Product
from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector
from django.urls import reverse

# Create your views here.

def home(request):

    return render(request, 'main_site/welcome_page.html')

def account_detail(request):
    favorite_message = "Produits favoris"

    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('user_management:signup'))

    favorite_products = request.user.product_set.all()
    if list(favorite_products) == []:
        favorite_message = "Vous n'avez aucun produit favori."

    context  = {
        "username" : request.user.username,
        "email" : request.user.email,
        "favorite_message" : favorite_message,
        "favorite_products" : favorite_products,
    }

    return render(request, 'main_site/account_detail.html', context)

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
        "substitute_products" : best_subsitute_products,
    }

    return render(request, 'main_site/product_description_page.html', context)

def product_research(request):
    no_repetition_result = []
    vectors = SearchVector('name', weight='A') + SearchVector('category__name', weight='B')
    query = SearchQuery(f'{request.GET.get("product_searched")}')

    research_result = Product.objects.annotate(rank=SearchRank(vectors, query)).order_by('-rank')

    for product in research_result:
        if product not in no_repetition_result:
            no_repetition_result.append(product)

    context = {"results": no_repetition_result}
    request.session['research_parameter'] = request.GET.get("product_searched")
    return render(request, 'main_site/product_research.html', context)

def add_favorite(request):
    product_id = request.POST.get("product_id")
    print(product_id)
    return HttpResponseRedirect(f'/research/?product_searched={request.session["research_parameter"]}')
