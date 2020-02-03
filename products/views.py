# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Product
from django.contrib.auth.decorators import login_required

@login_required(login_url="registration") ###Checks if user is logged in if not redirects to login page"""
def all_products(request):
    products = Product.objects.all()
    return render(request, "products.html", {"products": products})

