# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Blog
from .forms import BlogPostForm

#Creates a view that will return a list of Blogs that were published prior to 'now' and render them to the 'blogposts.html' template
def get_blogs(request):
    blogs = Blog.objects.filter(published_date__lte=timezone.now()
        ).order_by('-published_date')
    return render(request, "blogposts.html", {'blogs': blogs})

#Create a view that returns a single Blog object based on the blog ID (pk) and render it to the 'postdetail.html' template or retrurn a 404 error if blog not found 
def blog_detail(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    blog.views += 1
    blog.save()
    return render(request, "blogdetail.html", {'blog': blog})

#Create a view that allows a blog to be created or edited if the post ID is null or not
def create_or_edit_blog(request, pk=None):
    blog = get_object_or_404(Blog, pk=pk) if pk else None
    if request.method == "POST":
        form = BlogPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save()
            return redirect(post_detail, post.pk)
    else:
        form = BlogPostForm(instance=post)
    return render(request, 'blogpostform.html', {'form': form})


