from django.urls import path, include

from . import views

app_name = 'main_site'
urlpatterns = [
    path('', views.home, name='home'),
    path('aliment/<product_id>', views.product_description, name='product'),
]
