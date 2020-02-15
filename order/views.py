# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Cart

# Create your views here.
"""Renders the cart content page so user can view what their order"""
def view_order(request):
    return render(request, "cart.html")

