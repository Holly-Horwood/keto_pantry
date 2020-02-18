# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.models import User
from cart.models import Cart

# Create your views here.
"""Renders the cart content page"""
def view_cart(request):
    return render(request, "cart.html")
