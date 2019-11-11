# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from accounts.forms import UserLoginForm, UserLoginForm, UserRegistrationForm
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

    def test_login_username_and_password_required(self):
        form = UserLoginForm({'username': 'admin',
                              'password': 'password123'})
        self.assertTrue(form.is_valid())            

    def test_registration_redirects(self):
        response = self.client.get(self.registration_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_incorrect_form_does_not_register(self):
        response = self.client.post("/accounts/register", {
            'username': 'admin',
            'email': 'admin@example.com',
            'password1': 'password123',
            'password2': 'password456',
        })
        self.assertEqual(User.objects.count(), 0)    

         
    