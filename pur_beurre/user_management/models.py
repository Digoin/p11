from django.db import models
from django.contrib.auth.models import AbstractUser
from main_site.models import Product

class UserExtension(AbstractUser):
    email = models.EmailField(unique=True)

    REQUIRED_FIELDS = ['username']
    USERNAME_FIELD = 'email'
