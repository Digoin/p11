from django.test import TestCase, Client

from user_management.models import UserExtension


class TestViews(TestCase):

    def setUp(self):

        self.client = Client()

        # Setting up temporary test database

# Test signup
    def test_signup_method_get(self):
        response = self.client.get('/signup/')

        self.assertEqual(response.status_code, 200)

    def test_signup_method_post(self):
        user = UserExtension(id=1, username="martin", email="martin@internet.net", password = 'UltimatePassword56')
        response = self.client.post('/signup/', {
            'username':'martin',
            'email':'martin@internet.net', 
            'password1':'UltimatePassword56', 
            'password2':'UltimatePassword56'
        })

        self.assertRedirects(response, '/', status_code=302)
        self.assertEqual(UserExtension.objects.get(id = 1), user)
