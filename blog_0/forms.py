#-*- coding: utf-8 -*-
from django import forms
from .models import Article, Categorie

class ContactForm(forms.Form):
    sujet = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    envoyeur = forms.EmailField(label="Votre adresse mail")
    renvoi = forms.BooleanField(help_text="Cochez si vous souhaitez obtenir une copie du mail envoyé.", required=False)
    
#------------------------------

class CategorieForm(forms.ModelForm):

    class Meta:
        model = Categorie
        fields = ('__all__')

class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = ('__all__')


#------------------------------
