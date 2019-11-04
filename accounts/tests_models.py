# from django.test import TestCase, Client
# from .models import Cart, CartLineItem

# # Create your tests here.
# class CartTests(TestCase):
#     def setUp(self):
#         self.client = Client()
#         self.client.login(username='AutoTester', password='test12345')
    
#     def what_is_in_the_cart_test(self):
#         # simple example of model tests. add to each app the below can be changed up to for example look at products can extend whats there and check all fields are returning the right results
#         cart = CartLineItem.objects.create(cart='This is a test',
#                                             product=self.product,
#                                             quantity='Qty is 0')
#         #removed from here: .save() - b/c no need to save to the db for these tests

#         self.assertEqual(cart.cart, 'This is a test')
#         self.assertEqual(cart.product, 'This is a test')
#         self.assertEqual(cart.quantity, 'Qty is 0')
