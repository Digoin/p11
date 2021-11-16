import json
import requests

from django.core.management.base import BaseCommand, CommandError
from main_site.models import Category, Product
from ._product_maker import ApiProduct
from django.db import IntegrityError

class Command(BaseCommand):
    help = 'Fill the database with the specified categories and linked products'

    def add_arguments(self, parser):
        parser.add_argument('category_names', nargs='+', type=str)

    def products_list_creator(self, category):
        products_list = []
        api_request = dict(requests.get(f"https://fr-en.openfoodfacts.org/category/{category}.json").json())
        for json_product in api_request["products"]:
            product = ApiProduct(json_product)
            if self.product_data_validity(product):
                products_list.append(product)
        return products_list

    def product_data_validity(self, product):
        if (
            product.name() is None
            or product.categories() is None
            or product.nutriscore() is None
            or product.url() is None
            or product.categories_language() is None
        ):
            return False
        else:
            return True

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
            new_product = Product(name=product.name(), url=product.url(), nutriscore=product.nutriscore())
            try:
                new_product.save()
            except IntegrityError:
                self.stdout.write("Product already exist or his name is already used.")

    def handle(self, *args, **options):
        for category_name in options['category_names']:
            products_list = self.products_list_creator(category_name)
            self.fill_categories(products_list)
            self.fill_products(products_list)

        self.stdout.write(self.style.SUCCESS("Operation finished."))
