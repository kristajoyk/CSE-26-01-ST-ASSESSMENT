from django.db import models


class Product(models.Model):
    name     = models.CharField(max_length=200)
    category = models.CharField(max_length=100)
    price    = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()
    color    = models.CharField(max_length=100)
    image    = models.ImageField(upload_to='products/')

    def formatted_price(self):
        return "{:,}".format(self.price)

    def __str__(self):
        return self.name
