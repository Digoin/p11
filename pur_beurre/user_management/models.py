from django.db import models
from django.contrib.auth.models import AbstractUser
from main_site.models import Product

class UserExtension(AbstractUser):
    pass

    # favorites = models.ManyToManyField(Product)

    # USERNAME_FIELD = 'username'
    # REQUIRED_FIELDS = []
