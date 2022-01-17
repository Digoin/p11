from unittest import TestCase
from .._product_maker import ApiProduct

class TestProductMaker(TestCase):

# Similar functions
    def test_attribute_ok(self):
        test_input = {"product_name": "apple"}
        api_product = ApiProduct(test_input)

        test_result = "apple"

        assert test_result == api_product.name()
    
    def test_attribute_empty(self):
        test_input = {"product_name": ""}
        api_product = ApiProduct(test_input)

        test_result = None

        assert test_result == api_product.name()
    
    def test_attribute_dont_exist(self):
        test_input = {"product_id": "apple"}
        api_product = ApiProduct(test_input)

        test_result = None

        assert test_result == api_product.name()

# Categories tests
    def test_attribute_categories_ok(self):
        test_input = {"categories": "fruit,red"}
        api_product = ApiProduct(test_input)

        test_result = ["fruit", "red"]

        assert test_result == api_product.categories()

# Nutriscore tests
    def test_attribute_nutriscore_ok(self):
        test_input = {"nutrition_grades": "b"}
        api_product = ApiProduct(test_input)

        test_result = "B"

        assert test_result == api_product.nutriscore()

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
