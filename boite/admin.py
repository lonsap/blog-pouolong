# Register your models here.

from django.contrib import admin

from boite.models import Secteur_Activ, Metier_Activ, Forme_Juri, Adresse_Post, Respon_Boite, Entreprise, Evenement

class EntrepriseAdmin(admin.ModelAdmin):
    list_display   = ('raison_sociale', 'responsable', 'date_creation', 'apercu_description')
    list_filter    = ('responsable','secteur_activite',)
    date_hierarchy = 'date_creation'
    ordering       = ('date_creation', )
    search_fields  = ('raison_sociale', 'description')
   
   
    def saisie_direction(self, TitreDir, MereDir):
       # TitreDir : Titre de la direction
       # MereDir : Maison mère (raison sociale)
       if MereDir.direction == '':
           return self.libelle_dir+" : "+self.resp_dir
       else:
           return self.libelle_dir+" : "+self.resp_dir


    def apercu_description(self, soc):
       """ 
       Retourne les 40 premiers caractères de la description de l'entreprise. S'il
       y a plus de 40 caractères, il faut ajouter des points de suspension.
       """
       text = soc.description[0:40]
       if len(soc.description) > 40:
           return '%s...' % text
       else:
           return text

   # En-tête de notre colonne
    apercu_description.short_description = 'Aperçu de la description'
  
admin.site.register(Secteur_Activ)
admin.site.register(Metier_Activ)
admin.site.register(Forme_Juri)
admin.site.register(Adresse_Post)
admin.site.register(Evenement)
admin.site.register(Respon_Boite)
admin.site.register(Entreprise, EntrepriseAdmin)