# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.models import User
from .models import Cart, CartLineItem
from products.models import Product

# Create your views here.
# Renders the cart content page
def view_cart(request):
    return render(request, "cart.html")



# Add quantity of product to cart
def add_to_cart(request, product_id):
    quantity = int(request.POST.get('quantity'))

    cart = request.session.get('cart', {})
    cart_item_qty = cart.get(product_id)
    if cart_item_qty:
        cart[product_id] += quantity
    else:    
        cart[product_id] = cart.get(product_id, quantity)

    request.session['cart'] = cart
    #Persisting cart to database for logged in users
    if request.user.is_authenticated:
        cart_model, created = Cart.objects.get_or_create(
            user = User(id=request.user.id)
        )
        
        #Finds the matching product if none adds, updates quantity and saves to database
        cart_line_item, created = CartLineItem.objects.get_or_create(
            cart = Cart(id=cart_model.id),
            product = Product(id=product_id)
            )
        cart_line_item.quantity=quantity
        cart_line_item.save()

    return redirect(reverse('products'))
    
# Adjust quantity of product in cart
def adjust_cart(request, product_id):

    if request.POST.get('quantity').isdigit():

        quantity = int(request.POST.get('quantity'))
        cart = request.session.get('cart', {})

        #Persisting cart to database for logged in users
        if request.user.is_authenticated:
            cart_model, created = Cart.objects.get_or_create(
                user = User(id=request.user.id)
            )
            #Finds the matching product if none adds, updates quantity and saves to database
            cart_line_item, created = CartLineItem.objects.get_or_create(
                cart = Cart(id=cart_model.id),
                product = Product(id=product_id)
                )
            if quantity > 0:        
                cart_line_item.quantity=quantity
                cart_line_item.save()
            else:
                cart_line_item.delete()  

        #updates for session and removes deleted items from cart
        if quantity > 0:
            cart[product_id] = quantity
        else:
            cart.pop(product_id)
        
        request.session['cart'] = cart

    return redirect(reverse('view_cart'))


