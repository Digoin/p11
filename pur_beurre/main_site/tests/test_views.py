from django.test import LiveServerTestCase, TestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class HostTest(LiveServerTestCase, TestCase):

    def test_home(self):

        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get('http://127.0.0.1:8000')
        assert "Accueil" in driver.title

