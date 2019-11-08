# # -*- coding: utf-8 -*-
# from __future__ import unicode_literals

# from django.test import TestCase, Client
# from django.urls import reverse
# from django.conf.urls import url
# from .models import Post
# from .views import get_posts, post_detail, create_or_edit_post

# # Create your tests here.
# class TestBlogViews(TestCase):

#     def setUp(self):
#         self.Client = Client()
#         post_id = (Post, pk='1')

#     def test_get_posts(self):
#         self.get_posts_url = reverse('get_posts')
#         response = self.client.get(self.get_post_url)

#         self.assertEquals(response.status_code, 200)
#         self.assertTemplateUsed(response, 'blogposts.html')

#     def test_post_detail(self):
#         self.post_detail_url = reverse('post_detail' post_id)
#         response = self.client.get(self.post_detail_url)

#         self.assertEquals(response.status_code, 200)
#         self.assertTemplateUsed(response, 'postdetail.html')   

#     def test_create_or_edit_post(self):
#         self.create_or_edit_post_url = reverse('create_or_edit_post')
#         response = self.client.get(self.create_or_edit_post_url)

#         self.assertEquals(response.status_code, 200)
#         self.assertTemplateUsed(response, 'blogpostform.html')

