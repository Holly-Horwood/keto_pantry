from django.test import TestCase, Client
from django.db import models
from django.utils import timezone
from .models import Post

# Create your tests here.
class PostTests(TestCase):
    
    def setUp(self):
        self.client = Client()
        
    def what_is_in_the_post_test(self):
        post = Post.objects.create(title=self.title,
                                    author='Bob',
                                    published_date='12/10')

        self.assertEqual(post.title, 'This is a test')
        self.assertEqual(post.author, 'This is a test')
        self.assertEqual(post.published_date, 'Qty is 0')