# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from .views import add_to_cart, adjust_cart, delete_from_cart

# Create your tests here.
class TestCartViews(TestCase):

    def setUp(self):
        self.Client = Client()
        self.user = User.objects.create_user('bob', 'bob@bob.com', 'bobpassword')
        self.add_to_cart_url = reverse('products')
        self.adjust_cart_url = reverse('view_cart')
        self.delete_from_cart_url = reverse('view_cart')

    
    def test_add_to_cart_redirects(self):
        self.client.login(username='bob', password='bobpassword')
        response = self.client.get(self.add_to_cart_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'products.html')   

    def test_adjust_cart_redirects(self):
        response = self.client.get(self.adjust_cart_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'cart.html')

    def test_delete_from_cart_redirects(self):
        response = self.client.get(self.delete_from_cart_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'cart.html')    