# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase, Client
from .models import Product
from django.contrib.auth.models import User
from django.urls import reverse
from .views import all_products

# Create your tests here.
class TestProductViews(TestCase):

    def setUp(self):
        self.Client = Client()
        self.user = User.objects.create_user('bob', 'bob@bob.com', 'bobpassword')
        self.all_products_url = reverse('products')
        
    def test_add_to_cart_redirects(self):
        self.client.login(username='bob', password='bobpassword')
        response = self.client.get(self.all_products_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'products.html')   
    
    def test_str(self):
        test_name = Product(name='A product')
        self.assertEqual(str(test_name), 'A product')



