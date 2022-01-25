from django.test import TransactionTestCase
from unittest.mock import patch, MagicMock, Mock
from json import dumps

from ..filldatabase import Command
from .._product_maker import ApiProduct
from main_site.models import Product, Category

class TestCommand(TransactionTestCase):

    def setUp(self):

        self.command = Command()

        # Setting up products
        self.product1 = Product.objects.create(
            id=1,
            name="apple",
            url="apple_url",
            nutriscore="A",
            img_url="apple_img_url",
            kcal=101,
            fat=201,
            protein=301,
            sugar=401,
        )

        # Setting up categories
        self.category1 = Category.objects.create(name="fruit")

    # Test fill_categories
    def test_fill_categories_alright(self):
        product = ApiProduct
        product.categories = Mock(return_value=["fruit"])
        
        self.command.fill_categories([product])

        self.assertEqual(list(Category.objects.all()), [self.category1])

    def test_fill_categories_already_exist(self):
        product = ApiProduct
        self.category1.save()
        product.categories = Mock(return_value=["fruit"])
        
        self.command.fill_categories([product])

        self.assertEqual(list(Category.objects.all()), [self.category1])

    # Test fill_products
    def test_fill_products_alright(self):

        product = ApiProduct
        product.name = Mock(return_value="apple")
        product.url = Mock(return_value="apple_url")
        product.nutriscore = Mock(return_value="A")
        product.image_url = Mock(return_value="apple_img_url")
        product.kcal = Mock(return_value=101)
        product.fat = Mock(return_value=201)
        product.protein = Mock(return_value=301)
        product.sugar = Mock(return_value=401)

        self.command.fill_products([product])

        self.assertEqual(list(Product.objects.all()), [self.product1])

    def test_fill_products_already_exist(self):
        self.product1.save()

        product = ApiProduct
        product.name = Mock(return_value="apple")
        product.url = Mock(return_value="apple_url")
        product.nutriscore = Mock(return_value="A")
        product.image_url = Mock(return_value="apple_img_url")
        product.kcal = Mock(return_value=101)
        product.fat = Mock(return_value=201)
        product.protein = Mock(return_value=301)
        product.sugar = Mock(return_value=401)

        self.command.fill_products([product])

        self.assertEqual(list(Product.objects.all()), [self.product1])

    # Test link_product_categories
    def test_link_product(self):
        self.product1.save()
        self.category1.save()

        product = ApiProduct
        product.name = Mock(return_value="apple")
        product.categories = Mock(return_value=(["fruit"]))
        print(product.name(), product.categories())
        self.command.link_product_categories(product)

        self.assertEqual(list(self.category1.products.all()), [self.product1])


    # @patch('requests.get')
    # def test_products_list_creator(self, mock_get):
                
    #     test_json_product = dumps({"products":
    #         [
    #             {
    #                 "name": "apple",
    #             },
    #             {
    #                 "name": "banana",
    #             }
    #         ]
    #     }).encode('ascii')

    #     resp = Response()
    #     resp.encoding = 'ascii'
    #     resp._content = test_json_product

    #     mock_get.return_value = resp

    #     ApiProduct = MagicMock(return_value="product")
        
    #     self.command.product_data_validity = MagicMock(return_value=True)
        
    #     response = self.command.products_list_creator(None,None)
    #     assert [["product"],["product"]] == [response]

