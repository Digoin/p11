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

    # def test_signup_method_post(self):
    #     response = self.client.post('/signup/', {'username':'martin', 'email':'martin@internet.net', 'password1':'UltimatePassword56', 'password2':'UltimatePassword56'})

    #     self.assertRedirects(response, '/home/', status_code=302)
    #     self.assertEqual(list(UserExtension.objects.get()), [])
