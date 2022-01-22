import requests
from django.core.management.base import BaseCommand
from django.db import IntegrityError

from main_site.models import Category, Product
from ._product_maker import ApiProduct

class Command(BaseCommand):
    help = 'Fill the database with the specified categories and linked products'

    def add_arguments(self, parser):
        parser.add_argument('category_name', nargs='+', type=str)
        parser.add_argument('number_of_pages', nargs='+', type=int)

    def products_list_creator(self, category, number_of_pages):
        products_list = []
        api_request = dict(requests.get(f"https://fr-en.openfoodfacts.org/category/{category}/{number_of_pages}.json").json())
        for json_product in api_request["products"]:
            product = ApiProduct(json_product)
            if self.product_data_validity(product):
                products_list.append(product)
        return products_list

    def product_data_validity(self, product):
        return (
            product.name() is None
            or product.categories() is None
            or product.nutriscore() is None
            or product.url() is None
            or product.categories_language() is None
            or product.categories_language() != "fr"
            or product.image_url() is None
            or product.kcal() is None
            or product.fat() is None
            or product.protein() is None
            or product.sugar() is None
        )

    def fill_categories(self, products):
        for product in products:
            for category in product.categories():
                new_category = Category(name=category)
                try:
                    new_category.save()
                except IntegrityError:
                    self.stdout.write("Category already exist.")

    def fill_products(self, products):
        for product in products:
            new_product = Product(
                name=product.name(),
                url=product.url(),
                nutriscore=product.nutriscore(),
                img_url=product.image_url(),
                kcal=product.kcal(),
                fat=product.fat(),
                protein=product.protein(),
                sugar=product.sugar()
            )
            try:
                new_product.save()
                self.link_product_categories(product)
            except IntegrityError:
                self.stdout.write("Product already exist or his name is already used.")
    
    def link_product_categories(self, product):
            for category in product.categories():
                category_instance = Category.objects.filter(name=category)[0]
                product_instance = Product.objects.filter(name=product.name())[0]
                category_instance.products.add(product_instance)
                category_instance.save()

    def handle(self, *args, **options):
        for pages in range(1, options['number_of_pages'][0]):
            products_list = self.products_list_creator(options['category_name'], pages)
            self.fill_categories(products_list)
            self.fill_products(products_list)

        self.stdout.write(self.style.SUCCESS("Operation finished."))
