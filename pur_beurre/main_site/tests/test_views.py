from django.test import LiveServerTestCase, TestCase
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

class HostTest(LiveServerTestCase, TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def tearDown(self):
        self.driver.close()

    def test_new_user_reserach_and_add_favorite(self):
        driver = self.driver
        driver.get('http://127.0.0.1:8000')
        self.assertIn("Accueil", driver.title)

        search_bar = driver.find_element_by_name("product_searched")
        search_bar.send_keys("apple")
        search_bar.send_keys(Keys.ENTER)
        self.assertIn("Recherche", driver.title)


