from django.test import TestCase, Client
from django.contrib.auth.models import AnonymousUser

from user_management.models import UserExtension
from main_site.models import Product, Category


class TestViews(TestCase):

    def setUp(self):

        self.client = Client()

        # Setting up temporary test database

        # Setting up user
        self.user = UserExtension.objects.create(id=1, username="martin", email="martin@internet.net")
        self.user.set_password('secret')
        self.user.save()

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

        self.product2 = Product.objects.create(
            id=2,
            name="banana",
            url="banana_url",
            nutriscore="B",
            img_url="banana_img_url",
            kcal=102,
            fat=202,
            protein=302,
            sugar=402,
        )

        self.product3 = Product.objects.create(
            id=3,
            name="apple cake",
            url="apple_cake_url",
            nutriscore="C",
            img_url="apple_cake__img_url",
            kcal=103,
            fat=203,
            protein=303,
            sugar=403,
        )

        # Setting up categories
        self.category1 = Category.objects.create(name="fruit")
        self.category2 = Category.objects.create(name="cake")
        self.category1.products.set([self.product1, self.product2])
        self.category2.products.set([self.product3])


# Test account_detail
    def test_account_detail_not_authenticated(self):
        response = self.client.get('/account/')

        response.user = AnonymousUser()

        self.assertRedirects(response, '/signup/', status_code=302)

    def test_account_detail_authenticated(self):
        self.client.login(username="martin", password="secret")
        response = self.client.get('/account/')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["username"], "martin")
        self.assertEqual(response.context["email"], "martin@internet.net")

# Test product_description
    def test_product_description_not_authenticated_and_no_substitute(self):
        response = self.client.get('/aliment/1/')

        response.user = AnonymousUser()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['focused_product'], self.product1)
        self.assertEqual(response.context['substitute_products'], [])
        self.assertEqual(response.context['favorite_products'], [])

    def test_product_description_one_better_product_and_favorite(self):
        self.user.product_set.add(self.product2)
        self.client.login(username="martin", password="secret")
        response = self.client.get('/aliment/2/')
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['focused_product'], self.product2)
        self.assertEqual(response.context['substitute_products'], [self.product1])
        self.assertEqual(list(response.context['favorite_products']), [self.product2])

# Test product_research
    def test_product_research(self):
        response = self.client.get('/research/', {"product_searched": "apple"})

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['results'], [self.product1, self.product3, self.product2])

