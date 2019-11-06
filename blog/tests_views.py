# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase, Client
from django.urls import reverse
from django.conf.urls import url
from .models import Post
from .views import get_posts, post_detail, create_or_edit_post

# Create your tests here.
class TestBlogViews(TestCase):

    def setUp(self):
        self.Client = Client()
        self.get_posts_url = reverse('get_posts')
        self.post_detail_url = reverse('post_detail' pk)
        self.create_or_edit_post_url = reverse('create_or_edit_post')

    def test_get_posts(self):
        response = self.client.get(self.get_post_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'blogposts.html')

    def test_post_detail(self):
        response = self.client.get(self.post_detail_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'postdetail.html')   

    def test_create_or_edit_post(self):
        response = self.client.get(self.create_or_edit_post_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'blogpostform.html')

