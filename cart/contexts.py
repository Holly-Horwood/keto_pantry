from django.shortcuts import get_object_or_404
from products.models import Product
from .models import Cart

#Ensures cart items are available on every page  

def cart_contents(request):
    cartDict = request.session.get('cart', {})
    cart_items = []
    total = 0
    product_count = 0
    if cartDict:
        cart = Cart.objects.get(id=cartDict['id'])
        for cart_line_item in cart.cartlineitem_set.all():
            product = cart_line_item.product
            total += cart_line_item.quantity * product.price
            product_count += cart_line_item.quantity
            cart_items.append({'id': cart_line_item.id, 'quantity': cart_line_item.quantity, 'product': product})

    return {'cart_items': cart_items, 'total': total, 'product_count': product_count}