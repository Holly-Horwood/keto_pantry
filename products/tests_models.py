from django.test import TestCase, Client
from django.db import models
from .models import Product


# Create your tests here.
class ProductModelTests(TestCase):
    
    def setUp(self):
        self.client = Client()
        self.client.login(username='AutoTester', password='test12345')
    
    def what_is_in_the_product_class_test(self):
        product = Product.objects.create(name=self.name,
                                            price='12.50')

        self.assertEqual(product.name, self.name)
        self.assertEqual(product.price, '12.50')
        

      