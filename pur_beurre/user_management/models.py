from django.db import models
from django.contrib.auth.models import AbstractUser
from main_site.models import Product

class UserExtension(AbstractUser):

    email = models.EmailField(('email address'), unique=True)
    favorites = models.ManyToManyField(Product)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
