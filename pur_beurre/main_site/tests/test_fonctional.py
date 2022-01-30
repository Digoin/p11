import logging
from django.test import LiveServerTestCase
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from django.test import Client
import time
from user_management.models import UserExtension
from main_site.models import Product, Category



class HostTest(LiveServerTestCase):


    def setUp(self):

        self.client = Client()

        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

        # Setting up temporary test database

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

    def tearDown(self):
        self.driver.close()

    def test_new_user_reserach_and_add_favorite(self):
        driver = self.driver
        driver.get(self.live_server_url)
        self.assertIn("Accueil", driver.title)

        search_bar = driver.find_element_by_name("product_searched")
        search_bar.send_keys("apple")
        search_bar.send_keys(Keys.ENTER)
        self.assertIn("Recherche", driver.title)

        product = driver.find_element_by_class_name('product-presentation')
        product.click()

        product_title = driver.find_element_by_xpath('//div/h2[1]').text
        self.assertEqual("apple", product_title)

        add_favorite = driver.find_element_by_class_name('disk-button')
        add_favorite.click()
        self.assertIn("Création de compte", driver.title)

        username_form = driver.find_element_by_name('username')
        email_form = driver.find_element_by_name('email')
        password1_form = driver.find_element_by_name('password1')
        password2_form = driver.find_element_by_name('password2')
        validation = driver.find_element_by_xpath('//p/button')

        username_form.send_keys("martinos")
        email_form.send_keys("martinos.martin@internet.net")
        password1_form.send_keys("GoodPassword123")
        password2_form.send_keys("GoodPassword123")
        validation.send_keys(Keys.ENTER)
        self.assertIn("Accueil", driver.title)

        search_bar = driver.find_element_by_name("product_searched")
        search_bar.send_keys("apple")
        search_bar.send_keys(Keys.ENTER)
        self.assertIn("Recherche", driver.title)

        product = driver.find_element_by_class_name('product-presentation')
        product.click()

        product_title = driver.find_element_by_xpath('//div/h2[1]').text
        self.assertEqual("apple", product_title)

        add_favorite = driver.find_element_by_class_name('disk-button')
        add_favorite.click()

        favorite_link = driver.find_element_by_xpath('//a[3]')
        favorite_link.click()

        product_title = driver.find_element_by_xpath('//div/h2[1]').text
        self.assertEqual("apple", product_title)

