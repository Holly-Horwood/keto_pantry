# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase, Client
from .models import Cart

# Create your tests here.
class CartTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.client.login(username='AutoTester', password='test12345')
    
    ###
    # MODEL TESTS
    ###
    def cart_test(self):
        # simple example of model tests. add to each app the below can be changed up to for example look at products can extend whats there and check all fields are returning the right results
        bug = Bugs.objects.create(name="Test Bug Form",
                                  description='This is a test',
                                  username=self.user,
                                  picture=pic)
        #removed from here: .save() - b/c no need to save to the db for these tests

        self.assertEqual(bug.name, 'Test Bug Form')
        self.assertEqual(bug.description, 'This is a test')
        self.assertEqual(str(bug.username), 'testuser')
        self.assertEqual(bug.status, 'Waiting')

    ###
    # PAGE TESTS
    ###
    # Tests their view.cart page is found TODO: ref bretties other https://github.com/brettcutt/issue-tracker/blob/master/bugs/test_views.py
    def test_that_finds_view_cart_page(self):
        response = self.client.get('/cart/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cart.html') 
