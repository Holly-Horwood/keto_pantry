# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from products.models import Product

# Create your models here.
class Cart(models.Model):
    user = models.ForeignKey(User, null=False)
    
    def __str__(self):
        return "{0}-{1}".format(self.id, self.user)


class CartLineItem(models.Model):
    cart = models.ForeignKey(Cart, null=False)
    product = models.ForeignKey(Product, null=False)
    quantity = models.IntegerField(default=0)
    
    def __str__(self):
        return "{0} {1} {2}".format(
            self.quantity, self.product.name, self.product.price)


