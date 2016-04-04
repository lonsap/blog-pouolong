# Register your models here.

from django.contrib import admin
from blog.models import Categorie, Article

class ArticleAdmin(admin.ModelAdmin):
    list_display   = ('titre', 'auteur', 'date_publication')
    list_filter    = ('auteur','categorie',)
    date_hierarchy = 'date_publication'
    ordering       = ('date_publication', )
    search_fields  = ('titre', 'contenu')

    def apercu_contenu(self, article):
        """ 
        Retourne les 40 premiers caractères du contenu de l'article. S'il
        y a plus de 40 caractères, il faut ajouter des points de suspension.
        """
        text = article.contenu[0:40]
        if len(article.contenu) > 40:
            return '%s...' % text
        else:
            return text
        
    # En-tête de notre colonne
    apercu_contenu.short_description = 'Aperçu du contenu'
  
admin.site.register(Categorie)
admin.site.register(Article, ArticleAdmin)