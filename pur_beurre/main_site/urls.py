from django.urls import path

from . import views

app_name = 'main_site'
urlpatterns = [
    path('', views.home, name='home'),
    path('aliment/<product_id>/', views.product_description, name='product'),
    path('notice/', views.legal_notice, name='notice'),
    path('research/', views.product_research, name='research'),
    path('research_category/', views.category_research, name='research_category'),
    path('category_products/<category_id>/', views.products_of_category, name='category_products'),
    path('account/', views.account_detail, name='account'),
    path('favorites/', views.favorites, name='favorites'),
    path('add-favorite/', views.add_favorite, name='add-favorite')
]
