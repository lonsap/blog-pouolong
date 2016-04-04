from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from .models import Post, Contact
from .forms import PostForm
from django.shortcuts import redirect
from datetime import datetime


def post_list(request):
    posts = Post.objects.all().order_by('published_date')
#    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts, 'date': datetime.now()})
    
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post, 'date': datetime.now()})
    
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('blog.views.post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})
    
    
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('blog.views.post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})
    
def nouveau_contact(request):
    sauvegarde = False

    if request.method == "POST":
        form = NouveauContactForm(request.POST, request.FILES)
        if form.is_valid():
            contact = Contact()
            contact.nom = form.cleaned_data["nom"]
            contact.adresse = form.cleaned_data["adresse"]
            contact.photo = form.cleaned_data["photo"]
            contact.save()

            sauvegarde = True
    else:
        form = NouveauContactForm()

    return render(request, 'contact.html', locals())    
    
    
def voir_contacts(request):
    contacts = Contact.objects.all()
    return render(request, 'blog/voir_contacts.html', {'contacts': contacts})