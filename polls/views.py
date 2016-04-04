# -*- coding: Latin-1 -*-

# --- from django.shortcuts import render

# Create your views here.

# ---------------- Apport --------------

#
# Create your views here.

from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render
from django.http import Http404
#from blog.models import Entreprise
from django.shortcuts import render, get_object_or_404
#from blog.forms import ContactForm
from .models import Question, Choice


def date_actuelle(request):
    return render(request, 'blog/date.html', {'date': datetime.now(), 'prenom':'Etienne'})

def addition(request, nombre1, nombre2):    
    total = int(nombre1) + int(nombre2)
    #------------- Retourne nombre1, nombre2 et la somme des deux au tpl
    return render(request, 'blog/addition.html', locals())
    
def index(request):
    return render(request, 'contact.html', locals())

def menus_polls(request):
    valeur ='TROP C TROP'
    return render(request, 'polls/menus_polls.html', locals())

def accueil(request):
    """ Afficher tous les articles de notre blog """
    articles = Article.objects.all() # Nous sélectionnons tous nos articles
    return render(request, 'blog/accueil.html', {'derniers_articles': articles})

def lire(request, id, slug):
    article = get_object_or_404(Article, id=id, slug=slug)
    return render(request, 'blog/lire.html', {'article':article})


def contact(request):
    if request.method == 'POST':  # S'il s'agit d'une requête POST
        form = ContactForm(request.POST)  # Nous reprenons les données

        if form.is_valid(): # Nous vérifions que les données envoyées sont valides

            # Ici nous pouvons traiter les données du formulaire
            sujet = form.cleaned_data['sujet']
            message = form.cleaned_data['message']
            envoyeur = form.cleaned_data['envoyeur']
            renvoi = form.cleaned_data['renvoi']

            # Nous pourrions ici envoyer l'e-mail grâce aux données que nous venons de récupérer

            envoi = True

    else: # Si ce n'est pas du POST, c'est probablement une requête GET
        form = ContactForm()  # Nous créons un formulaire vide

    return render(request, 'contact.html', locals())
 
def article(request):
    if request.method == 'POST':  # S'il s'agit d'une requête POST
        form = ArticleForm(request.POST)  # Nous reprenons les données
 
        if form.is_valid(): # Nous vérifions que les données envoyées sont valides
 
            # Ici nous pouvons traiter les données du formulaire
            titre = form.cleaned_data['titre']
            auteur = form.cleaned_data['auteur']
            slug = form.cleaned_data['slug']
            contenu = form.cleaned_data['contenu']
            categorie = form.cleaned_data['categorie']
 
            # Nous pourrions ici envoyer l'e-mail grâce aux données que nous venons de récupérer
 
            envoi = True
 
    else: # Si ce n'est pas du POST, c'est probablement une requête GET
        form = ArticleForm()  # Nous créons un formulaire vide
 
    return render(request, 'blog/contact.html', locals())
 
#-------------------------------


def essai_00(request):
    questions=None
    if request.GET.get('search'):
        search = request.GET.get('search')
        questions = Question.objects.filter(question_text__icontains=search)

        name = request.GET.get('name')
        value = Question.objects.create(question_text=search, user=name)
#        pub_date = timezone.now()
        value.save()

    return render(request, 'essai_00.html',{
        'questions': questions,
    })

#-------------------------------
 
 
#   try:
#        article = Article.objects.get(id=id)
#    except Article.DoesNotExist:
#        raise Http404

#    return render(request, 'blog/lire.html', {'article': article})
