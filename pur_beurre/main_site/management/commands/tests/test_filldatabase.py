from unittest import TestCase
from unittest.mock import patch
from ..filldatabase import Command

# class TestCommand(TestCase):

#     @patch('self.product_data_validity')
#     @patch('ApiProduct')
#     @patch('requests.get')
#     def test_products_list_creator(self, mock_get, mock_product, mock_validity):
#         mock_get.return_value = {"products":
#         {
#             "name": "apple",
#             "categories": "apple,red"
#         }
#         }
#         mock_product.return_value = "test"
#         mock_validity.return_value = True

#         command = Command

#         assert ["test","test"] == command.products_list_creator(None,None)
