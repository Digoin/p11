import string
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from main_site.models import Product
from django.contrib.postgres.search import TrigramWordSimilarity
from django.urls import reverse

# Create your views here.

def home(request):

    return render(request, 'main_site/welcome_page.html')

def account_detail(request):

    # Checking if user is authentificated
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('user_management:signup'))

    context  = {
        "username" : request.user.username,
        "email" : request.user.email
    }

    return render(request, 'main_site/account_detail.html', context)

def legal_notice(request):

    return render(request, 'main_site/legal_notice.html')
  
def product_description(request, product_id):
    favorite_products = []
    substitute_products = []
    best_subsitute_products = []
    nutriscore_count = 0
    product = Product.objects.get(id=product_id)

    # Checking if user is authentificated
    if request.user.is_authenticated:
        favorite_products = request.user.product_set.all()

    # Creating the list of products with better nutriscore than the main one
    for categories in product.category_set.all():
        for linked_product in categories.products.all():
            if string.ascii_uppercase.index(linked_product.nutriscore) <= string.ascii_uppercase.index(product.nutriscore) and linked_product not in substitute_products and linked_product != product:
                substitute_products.append(linked_product)

    # Creating the list with the bests nutriscore from the first list
    while nutriscore_count < 4:
        for best_product in substitute_products:
            if len(best_subsitute_products) >= 6:
                break
            if string.ascii_uppercase.index(best_product.nutriscore) == nutriscore_count:
                best_subsitute_products.append(best_product)
        nutriscore_count += 1

    context = {
        "focused_product" : product,
        "substitute_products" : best_subsitute_products,
        "favorite_products" : favorite_products,
    }

    return render(request, 'main_site/product_description_page.html', context)

def product_research(request):
    no_repetition_result = []

    # Executing the research
    research_result = Product.objects.annotate(
        similarity=TrigramWordSimilarity(f'{request.GET.get("product_searched")}', "name")
    ).filter(similarity__gte=0.5).order_by('-similarity')

    # Creating a list without repetitions
    for product in research_result:
        if product not in no_repetition_result:
            no_repetition_result.append(product)

    context = {
        "results": no_repetition_result,
    }

    return render(request, 'main_site/product_research.html', context)

def favorites(request):
    favorite_message = "Produits favoris"

    # Checking if user is authentificated
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('user_management:login'))

    favorite_products = request.user.product_set.all()

    if list(favorite_products) == []:
        favorite_message = "Vous n'avez aucun produit favori"

    context  = {
        "favorite_message" : favorite_message,
        "favorite_products" : favorite_products,
    }

    return render(request, 'main_site/favorite_page.html', context)

def add_favorite(request):
    
    # Checking if user is authenticated
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('user_management:signup'))

    product_id = request.POST.get("product_id")
    product = Product.objects.get(id=product_id)
    user_connected = request.user
    favorite_products = user_connected.product_set.all()

    if product not in favorite_products:
        product.users.add(user_connected)
    else:
        product.users.remove(user_connected)

    return HttpResponseRedirect(f'/aliment/{product_id}/')
