from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=200, unique=True)
    url = models.CharField(max_length=200, unique=True)
    nutriscore = models.CharField(max_length=1)
    users = models.ManyToManyField(User)
    img_url = models.CharField(max_length=200, unique=True)
    kcal = models.IntegerField()
    fat = models.IntegerField()
    protein = models.IntegerField()
    sugar = models.IntegerField()
    
    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)
    products = models.ManyToManyField(Product)

    def __str__(self):
        return self.name
