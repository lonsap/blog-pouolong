#-*- coding: utf-8 -*-
from django.shortcuts import render
from datetime import datetime
from blog.forms import ContactForm


from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from .models import Article
from .forms import ArticleForm
from django.shortcuts import redirect

# Create your views here.
from django.http import HttpResponse
    
def post_list(request):
    posts = Article.objects.all().order_by('date_publication')
#    posts = Article.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})

        
def post_detail(request, pk):
    post = get_object_or_404(Article, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})
        
def post_new(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.auteur = request.user
            post.date_publication = timezone.now()
            post.save()
            return redirect('blog.views.post_detail', pk=post.pk)
    else:
        form = ArticleForm()
    return render(request, 'blog/post_edit.html', {'form': form})
        
        
def post_edit(request, pk):
    post = get_object_or_404(Article, pk=pk)
    if request.method == "POST":
        form = ArticleForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.auteur = request.user
            post.date_publication = timezone.now()
            post.save()
            return redirect('blog.views.post_detail', pk=post.pk)
    else:
        form = ArticleForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})
