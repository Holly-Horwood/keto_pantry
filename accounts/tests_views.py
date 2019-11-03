# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase, Client
from django.urls import reverse
from .views import logout, login, registration

# Create your tests here.
class TestAccountViews(TestCase):

    def setUp(self):
        self.Client = Client()
        self.logout_url = reverse('index')
        self.login_url = reverse('index')
        self.registration_url = reverse('index')

    def test_logout_redirects(self):
        response = self.client.get(self.logout_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_login_redirects(self):
        response = self.client.get(self.logout_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')   

    def test_registration_redirects(self):
        response = self.client.get(self.registration_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

         
    