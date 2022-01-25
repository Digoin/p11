from django.test import LiveServerTestCase, TestCase
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

class HostTest(LiveServerTestCase, TestCase):

    def test_home(self):
        s=Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=s)
        driver.get('http://127.0.0.1:8000')
        self.assertIn("Accueil", driver.title)
