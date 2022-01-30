from django.test import TestCase
from .._product_maker import ApiProduct

class TestProductMaker(TestCase):

# Name tests
    def test_name_attribute_ok(self):
        test_input = {"product_name": "apple"}
        api_product = ApiProduct(test_input)

        test_result = "apple"

        assert test_result == api_product.name()
    
    def test_name_attribute_empty(self):
        test_input = {"product_name": ""}
        api_product = ApiProduct(test_input)

        test_result = None

        assert test_result == api_product.name()
    
    def test_name_attribute_dont_exist(self):
        test_input = {"product_id": "apple"}
        api_product = ApiProduct(test_input)

        test_result = None

        assert test_result == api_product.name()

# Categories tests
    def test_categories_attribute_ok(self):
        test_input = {"categories": "fruit, cake"}
        api_product = ApiProduct(test_input)

        test_result = ["fruit", "cake"]

        assert test_result == api_product.categories()
    
    def test_categories_attribute_empty(self):
        test_input = {"categories": ""}
        api_product = ApiProduct(test_input)

        test_result = None

        assert test_result == api_product.categories()
    
    def test_categories_attribute_dont_exist(self):
        test_input = {"categories_id": "fruit, cake"}
        api_product = ApiProduct(test_input)

        test_result = None

        assert test_result == api_product.categories()

# Nutriscore tests
    def test_nutriscore_attribute_ok(self):
        test_input = {"nutrition_grades": "a"}
        api_product = ApiProduct(test_input)

        test_result = "A"

        assert test_result == api_product.nutriscore()
    
    def test_nutriscore_attribute_empty(self):
        test_input = {"nutrition_grades": ""}
        api_product = ApiProduct(test_input)

        test_result = None

        assert test_result == api_product.nutriscore()
    
    def test_nutriscore_attribute_dont_exist(self):
        test_input = {"nutriscore": "a"}
        api_product = ApiProduct(test_input)

        test_result = None

        assert test_result == api_product.nutriscore()

# Url tests
    def test_url_attribute_ok(self):
        test_input = {"url": "https://fr-en.openfoodfacts.org/category/cakes.json"}
        api_product = ApiProduct(test_input)

        test_result = "https://fr-en.openfoodfacts.org/category/cakes.json"

        assert test_result == api_product.url()
    
    def test_url_attribute_empty(self):
        test_input = {"url": ""}
        api_product = ApiProduct(test_input)

        test_result = None

        assert test_result == api_product.url()
    
    def test_url_attribute_dont_exist(self):
        test_input = {"urls": "https://fr-en.openfoodfacts.org/category/cakes.json"}
        api_product = ApiProduct(test_input)

        test_result = None

        assert test_result == api_product.url()

# Categories language tests
    def test_attribute_categories_language_ok(self):
        test_input = {"categories_lc": "fr"}
        api_product = ApiProduct(test_input)

        test_result = "fr"

        assert test_result == api_product.categories_language()

    def test_attribute_categories_language_false(self):
        test_input = {"categories_lc": "de"}
        api_product = ApiProduct(test_input)

        test_result = None

        assert test_result == api_product.categories_language()

    def test_categories_language_attribute_empty(self):
        test_input = {"categories_lc": ""}
        api_product = ApiProduct(test_input)

        test_result = None

        assert test_result == api_product.categories_language()
    
    def test_categories_language_attribute_dont_exist(self):
        test_input = {"categories_languages": "fr"}
        api_product = ApiProduct(test_input)

        test_result = None

        assert test_result == api_product.categories_language()

# Image_url tests
    def test_image_url_attribute_ok(self):
        test_input = {"image_url": "https://fr-en.openfoodfacts.org/category/cakes.json"}
        api_product = ApiProduct(test_input)

        test_result = "https://fr-en.openfoodfacts.org/category/cakes.json"

        assert test_result == api_product.image_url()
    
    def test_image_url_attribute_empty(self):
        test_input = {"image_url": ""}
        api_product = ApiProduct(test_input)

        test_result = None

        assert test_result == api_product.image_url()
    
    def test_image_url_attribute_dont_exist(self):
        test_input = {"images_url": "https://fr-en.openfoodfacts.org/category/cakes.json"}
        api_product = ApiProduct(test_input)

        test_result = None

        assert test_result == api_product.image_url()

# Kcal tests
    def test_kcal_attribute_ok(self):
        test_input = {"nutriments" : {"energy-kcal_100g": "100"}}
        api_product = ApiProduct(test_input)

        test_result = "100"

        assert test_result == api_product.kcal()
    
    def test_kcal_attribute_empty(self):
        test_input = {"nutriments" : {"energy-kcal_100": ""}}
        api_product = ApiProduct(test_input)

        test_result = None

        assert test_result == api_product.kcal()
    
    def test_kcal_attribute_dont_exist(self):
        test_input = {"nutriment" : {"energy-kcal_100g": "100"}}
        api_product = ApiProduct(test_input)

        test_result = None

        assert test_result == api_product.kcal()

# Fat tests
    def test_fat_attribute_ok(self):
        test_input = {"nutriments" : {"fat_100g": "100"}}
        api_product = ApiProduct(test_input)

        test_result = "100"

        assert test_result == api_product.fat()
    
    def test_fat_attribute_empty(self):
        test_input = {"nutriments" : {"fat_100g": ""}}
        api_product = ApiProduct(test_input)

        test_result = None

        assert test_result == api_product.fat()
    
    def test_fat_attribute_dont_exist(self):
        test_input = {"nutriments" : {"fat_100": "100"}}
        api_product = ApiProduct(test_input)

        test_result = None

        assert test_result == api_product.fat()

# Protein tests
    def test_protein_attribute_ok(self):
        test_input = {"nutriments" : {"proteins_100g": "100"}}
        api_product = ApiProduct(test_input)

        test_result = "100"

        assert test_result == api_product.protein()
    
    def test_protein_attribute_empty(self):
        test_input = {"nutriments" : {"proteins_100g": ""}}
        api_product = ApiProduct(test_input)

        test_result = None

        assert test_result == api_product.protein()
    
    def test_protein_attribute_dont_exist(self):
        test_input = {"nutriments" : {"protein_100g": "100"}}
        api_product = ApiProduct(test_input)

        test_result = None

        assert test_result == api_product.protein()

# Sugar tests
    def test_sugar_attribute_ok(self):
        test_input = {"nutriments" : {"sugars_100g": "100"}}
        api_product = ApiProduct(test_input)

        test_result = "100"

        assert test_result == api_product.sugar()
    
    def test_sugar_attribute_empty(self):
        test_input = {"nutriments" : {"sugars_100g": ""}}
        api_product = ApiProduct(test_input)

        test_result = None

        assert test_result == api_product.sugar()
    
    def test_sugar_attribute_dont_exist(self):
        test_input = {"nutriments" : {"sugar_100g": "100"}}
        api_product = ApiProduct(test_input)

        test_result = None

        assert test_result == api_product.sugar()
