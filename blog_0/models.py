#-*- coding: utf-8 -*-
from django.db import models

class Categorie(models.Model):
    nom = models.CharField(max_length=30)

    def __str__(self):
        return self.nom
        

class Article(models.Model):
    titre = models.CharField(max_length=100)
    auteur = models.CharField(max_length=42)
    contenu = models.TextField(null=True)
    date_publication = models.DateTimeField(auto_now_add=True, auto_now=False, 
                                verbose_name="Date de parution")
    categorie = models.ForeignKey('Categorie')


    def publication(self):
        self.date_publication = timezone.now()
        self.save()

    
    def __str__(self):
        """ 
        Cette méthode que nous définirons dans tous les modèles
        nous permettra de reconnaître facilement les différents objets que 
        nous traiterons plus tard et dans l'administration
        """
        return self.titre
