from django.shortcuts import get_object_or_404
from products.models import Product
from .models import Cart

#Ensures cart items are available on every page  

def cart_contents(request):      

    cart = request.session.get('cart', {})        
    cart_items = []      
    total = 0      
    product_count = 0            

    if request.user.is_authenticated:
        for id, quantity in cart.items():          
            product = get_object_or_404(Product, pk=product_id)          
            total += quantity * product.price          
            product_count += quantity          

        cart_items.append({'id': id, 'quantity': quantity, 'product': product})            
    return {'cart_items': cart_items, 'total': total, 'product_count': product_count}