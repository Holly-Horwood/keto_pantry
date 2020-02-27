# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import stripe
from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.forms import model_to_dict
from .forms import MakePaymentForm, OrderForm
from .models import OrderLineItem
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import User
from products.models import Product
from cart.models import Cart
from cart.contexts import cart_contents



# Create your views here.
stripe.api_key = settings.STRIPE_SECRET


def checkout(request):
    if request.method == "POST":
        order_form = OrderForm(request.POST)
        payment_form = MakePaymentForm(request.POST)
        print("order form is valid:" + str(order_form.is_valid()))
        print("payment form is valid:" + str(payment_form.is_valid()))
        if order_form.is_valid() and payment_form.is_valid():
            order = order_form.save(commit=False)
            order.date = timezone.now()
            order.user = User(id=request.user.id)
            order.save()

            cart_contents(request)
            cartDict = request.session.get('cart', {})
            # cart_items = []
            #total = 0
            product_count = 0
            order.total = 0.0
            if cartDict:
                cart = Cart.objects.get(id=cartDict['id'])
                for cart_line_item in cart.cartlineitem_set.all():
                    product = cart_line_item.product
                    # total += cart_line_item.quantity * product.price
                    line_total = cart_line_item.quantity * product.price
                    order.total += line_total
                    product_count += cart_line_item.quantity
                    # cart_items.append({'id': cart_line_item.id, 'quantity': cart_line_item.quantity, 'product': product, 'line_total': line_total})
                    order_line_item = OrderLineItem(
                        order=order,
                        product=product,
                        quantity=product_count
                    )
                    order_line_item.save()
                    order.save()
            
            try:
                customer = stripe.Charge.create(
                    amount = int(order.total * 100),
                    currency  ="NZD",
                    description = order_form.cleaned_data['email'],
                    card = payment_form.cleaned_data['stripe_id']
                )

            except stripe.error.CardError:
                messages.error(request, "Your card was declined!")
            
            if customer.paid:

                messages.error(request, "Successfully Paid! View Order Below")
                request.session['cart'] = {}
                if request.user.is_authenticated:
                    try:
                        cart_model = Cart.objects.get(                  #trys to get cart by user id if it exists
                            user = User(id=request.user.id)
                        )
                        cart_model.delete()                             #if cart exists it will delete it 
                        
                        cart_get = Cart(user=request.user)
                        cart_get.save()                                 #creates a new cart
                        request.session['cart'] = model_to_dict(cart_get)  
                                                   
                    except Cart.DoesNotExist:
                        cart_model = None                               #if cart doesn't exist does nothing 
                
                return redirect(reverse('profile')) 
            else:
                messages.error(request, "Unable to take payment")
        else:
            print(payment_form.errors)
            messages.error(request, "We were unable to take a payment with that card!")
    else:
        payment_form = MakePaymentForm()
        order_form = OrderForm(initial={
            'email': request.user.email if request.user.is_authenticated else '' """will prepopulate if user is authenticated otherwise will leave blank"""
        })
    
    return render(request, "checkout.html", {"order_form": order_form, "payment_form": payment_form, "publishable": settings.STRIPE_PUBLISHABLE})

