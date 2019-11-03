# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from .views import checkout

# Create your tests here.
class TestCheckoutViews(TestCase):

    def setUp(self):
        self.Client = Client()
        self.user = User.objects.create_user('bob', 'bob@bob.com', 'bobpassword')
        self.checkout_url = reverse('checkout')
        
    def test_checkout_redirects(self):
        response = self.client.get(self.checkout_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'checkout.html')

    


