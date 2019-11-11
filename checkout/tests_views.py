# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.messages import get_messages
from django.urls import reverse
from .views import checkout
from .models import Order, OrderLineItem

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

    def test_credit_card_accepted(self):
        User.objects.create_user(
            username='admin',
            email='admin@example.com',
            password='password123')
        self.client.login(username='admin', password='password123')

        response = self.client.post('/checkout', {
            'credit_card_number': '4242424242424242',
            'cvv': '111',
            'expiry_month': '1',
            'expiry_year': '2021',
            }, follow=True)

        for message in get_messages(response.wsgi_request):
            self.assertNotEqual('Your card was declined!', messages)

        page = self.client.get("/products/")
        self.assertEqual(page.status_code, 200)

    


