from django.db import models

class Product(models.Model):
    product_name = models.CharField(max_length=30)
    product_weight = models.IntegerField()
    product_price = models.CharField(max_length=10)
    created_at = models.CharField(max_length=50)
    updated_at = models.CharField(max_length=50)