# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post
from .forms import BlogPostForm
from django.contrib.auth.decorators import login_required




#Creates a view and returns Blogs that were published prior to 'now' and renders them to the 'blogposts.html' template
def get_posts(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()
        ).order_by('-published_date')
    return render(request, "blogposts.html", {'posts': posts})

#Create a view that returns a single Post based on its ID and render it to the 'postdetail.html' template or return a 404 error 
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.views += 1
    post.save()
    return render(request, "postdetail.html", {'post': post})

#Create a view that where a blog post tcan be created or edited
@login_required #checks if the user is logged in
def create_or_edit_post(request, pk=None):
    post = get_object_or_404(Post, pk=pk) if pk else None
    if request.method == "POST":
        form = BlogPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save()
            return redirect(post_detail, post.pk)
    else:
        form = BlogPostForm(instance=post)
    return render(request, 'blogpostform.html', {'form': form})


