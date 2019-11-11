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
        pass
        
    def tearDown(self):
        pass 

    def test_get_posts_page_found(self):
        newPost = Post()
        newPost.title='test'
        newPost.author='test_author'
        newPost.content='test_content'
        newPost.save()
        get_posts_url = reverse('get_posts')
        response = self.client.get(get_posts_url)
        self.assertEqual(response.status_code, 200, "get_posts returned status code %s should be 200" % str(response.status_code)) 

    def test_post_detail_page_found(self):
        newPost = Post()
        newPost.title='test'
        newPost.author='test_author'
        newPost.content='test_content'
        newPost.save()
        post_detail_url = reverse('post_detail', args=[newPost.pk])
        response = self.client.get(post_detail_url)
        self.assertEqual(response.status_code, 200, "post_detail returned status code %s should be 200" % str(response.status_code))

    

