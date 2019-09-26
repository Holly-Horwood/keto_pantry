# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase, Client
from .models import Cart, CartLineItem

# Create your tests here.
class CartTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.client.login(username='AutoTester', password='test12345')
    
    ###
    # MODEL TESTS
    ###
    def what_is_in_the_cart_test(self):
        # simple example of model tests. add to each app the below can be changed up to for example look at products can extend whats there and check all fields are returning the right results
        cart = CartLineItem.objects.create(cart='This is a test',
                                            product=self.product,
                                            quantity='Qty is 0')
        #removed from here: .save() - b/c no need to save to the db for these tests

        self.assertEqual(cart.cart, 'This is a test')
        self.assertEqual(cart.product, 'This is a test')
        self.assertEqual(cart.quantity, 'Qty is 0')
        
    ###
    # PAGE TESTS
    ###
    # Tests their view.cart page is found TODO: ref bretties other https://github.com/brettcutt/issue-tracker/blob/master/bugs/test_views.py
    def test_that_finds_view_cart_page(self):
        response = self.client.get('/cart/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cart.html') 
