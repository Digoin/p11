from django.test import TestCase
from unittest.mock import patch, MagicMock
from json import dumps

from ..filldatabase import Command
from .._product_maker import ApiProduct

class TestCommand(TestCase):

    def setUp(self):
        self.command = Command()


    @patch('requests.get')
    def test_products_list_creator(self, mock_get):
                
        mock_get.return_value = dumps({"products":
            {
                "name": "apple",
                "categories": "fruit,red"
            }
        })

        api_product = ApiProduct
        api_product.name = MagicMock(return_value="apple")
        api_product.categories = MagicMock(return_value="fruit, red")

        self.command.product_data_validity = MagicMock(return_value=True)

        assert ["apple","fruit, red"] == self.command.products_list_creator(None,None)

