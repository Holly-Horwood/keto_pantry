from django.test import TestCase, Client
from django.db import models
from products.models import Product
from .models import Order, OrderLineItem


# Create your tests here.
class CheckoutModelTests(TestCase):
    
    def setUp(self):
        self.client = Client()
        self.client.login(username='AutoTester', password='test12345')
    
    def what_is_in_the_order_class_test(self):
        order = Order.objects.create(order='This is a test',
                                            id=self.id,
                                            country='New Zealand')

        self.assertEqual(order.order, 'This is a test')
        self.assertEqual(order.id, 'This is a test')
        self.assertEqual(order.country, 'New Zealand')

    def what_is_in_the_orderlineitem_class_test(self):
        orderlineitem = OrderLineItem.objects.create(order='This is a test',
                                            product=self.product,
                                            quantity='0')

        self.assertEqual(orderlineitem.order, 'This is a test')
        self.assertEqual(orderlineitem.id, 'This is a test')
        self.assertEqual(orderlineitem.country, '0')    