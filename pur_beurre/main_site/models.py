from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=200, unique=True)
    url = models.CharField(max_length=200, unique=True)
    nutriscore = models.CharField(max_length=1)
    users = models.ManyToManyField(User)
    
    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)
    products = models.ManyToManyField(Product)

    def __str__(self):
        return self.name
