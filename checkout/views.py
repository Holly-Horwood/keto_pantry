# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import MakePaymentForm, OrderForm
from .models import OrderLineItem
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import User
from products.models import Product
from cart.models import Cart
import stripe

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
            order.save()

            cart = request.session.get('cart', {})
            total = 0
            for id, quantity in cart.items():
                product = get_object_or_404(Product, pk=id)
                total += quantity * product.price
                order_line_item = OrderLineItem(
                    order=order,
                    product=product,
                    quantity=quantity
                )
                order_line_item.save()
            
            try:
                customer = stripe.Charge.create(
                    amount = int(total * 100),
                    currency  ="NZD",
                    description = order_form.cleaned_data['email'],
                    card = payment_form.cleaned_data['stripe_id']
                )

            except stripe.error.CardError:
                messages.error(request, "Your card was declined!")
            
            if customer.paid:

                messages.error(request, "You have successfully paid")
                request.session['cart'] = {}
                if request.user.is_authenticated:
                    try:
                        cart_model = Cart.objects.get(                  #trys to get cart by user id if it exists
                            user = User(id=request.user.id)
                        )
                        cart_model.delete()                             #if cart exists it will delete it 
                    except Cart.DoesNotExist:
                        cart_model = None                               #if cart doesn't exist does nothing    
                
                return redirect(reverse('products'))
            else:
                messages.error(request, "Unable to take payment")
        else:
            print(payment_form.errors)
            messages.error(request, "We were unable to take a payment with that card!")
    else:
        payment_form = MakePaymentForm()
        order_form = OrderForm(initial={
            'email': request.user.email if request.user.is_authenticated else '' #will prepopulate if user is authenticated otherwise will leave blank
        })
    
    return render(request, "checkout.html", {"order_form": order_form, "payment_form": payment_form, "publishable": settings.STRIPE_PUBLISHABLE})

