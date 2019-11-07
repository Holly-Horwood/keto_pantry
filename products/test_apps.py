from django.apps import apps
from django.test import TestCase
from .apps import ProductConfig


class TestProductConfig(TestCase):

    def test_product_app(self):
        self.assertEqual("product", ProductConfig.name)
        self.assertEqual("product", apps.get_app_config("product").name)