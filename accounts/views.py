# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required #will block users who are not logged in from seeing the logout page
from django.contrib.auth.models import User
from django.forms import model_to_dict
from accounts.forms import UserLoginForm, UserLoginForm, UserRegistrationForm
from cart.models import Cart, CartLineItem
from products.models import Product

def index(request):
    """Return the index.html file"""
    return render(request,  'index.html')

@login_required #checks if the user is logged in
def logout(request):
    """Log the user out"""
    auth.logout(request)
    messages.success(request, "You have been successfully logged out")
    return redirect(reverse('index'))    

def login(request):
    """Return a login page"""
    if request.user.is_authenticated:
        return redirect(reverse('index'))
    if request.method == "POST":
        login_form = UserLoginForm(request.POST)
        if login_form.is_valid():
            user = auth.authenticate(username=request.POST['username'],
                                    password=request.POST['password'])  
            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have successfully logged in!")

                # Check if user has a cart, create it if necessary
                try:
                    cart_get = Cart.objects.get(    # Gets an existing cart
                        user=user)                      
                    for cartLineItem in cart_get.cartlineitem_set.all():
                        print(cartLineItem)
                    
                except Cart.DoesNotExist:
                    cart_get = Cart(user=user)
                    cart_get.save()             # Create a new Cart
                request.session['cart'] = model_to_dict(cart_get)
                    
                return redirect(reverse('index')) 
            
            else:
                login_form.add_error(None, "Your username or password is incorrect")
    
    else:
        login_form = UserLoginForm()
    return render(request, 'login.html', {'login_form': login_form})

def registration(request):
    """Render the registration page"""
    if request.user.is_authenticated:
        return redirect(reverse('index'))

    if request.method == "POST":
        registration_form = UserRegistrationForm(request.POST)

        if registration_form.is_valid():
            registration_form.save()

            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password1'])
            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have successfully registered") 
            else:
                messages.error(request, "Unable to register your account at this time")
    else:
        registration_form = UserRegistrationForm()
    return render(request, 'registration.html', {
        "registration_form": registration_form})




