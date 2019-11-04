from django.test import TestCase, Client
from django.db import models
from django.contrib.auth.models import User
from products.models import Product
from .models import Cart, CartLineItem

# Create your tests here.
class CartTests(TestCase):
    
    def setUp(self):
        self.client = Client()
        self.client.login(username='AutoTester', password='test12345')
    
    def what_is_in_the_cart_test(self):
        cart = CartLineItem.objects.create(cart='This is a test',
                                            product=self.product,
                                            quantity='Qty is 0')

        self.assertEqual(cart.cart, 'This is a test')
        self.assertEqual(cart.product, 'This is a test')
        self.assertEqual(cart.quantity, 'Qty is 0')

    
    