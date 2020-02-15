from django.conf.urls import url
from cart.views import view_cart
from .views import view_order

urlpatterns = [
    url(r'^$', view_order, name='view_order'),
    url(r'^cart', view_cart, name='view_cart')
]