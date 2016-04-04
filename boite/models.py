#-*- coding: utf-8 -*-
from django.db import models

# Create your models here.

class Secteur_Activ(models.Model):
    libelle_sect = models.CharField(max_length=42)		# Nom du Secteur d'activité
    description_sect = models.TextField(null=True)
    
    def __str__(self):
        """ 
        Cette méthode décrit le secteur d'activité auquel appartient l'entreprise.
        Un secteur d'activité économique est le regroupement des entreprises de fabrication,d'industrie,
        de commerce ou de service qui ont la même activité principale
        (au regard de la nomenclature d'activité économique considérée) (définition Wikipédia)
        """
        return self.libelle_sect

class Metier_Activ(models.Model):
    libelle_meti = models.CharField(max_length=42)		# Nom du Métier (ou sous-secteur d'activité)
    description_meti = models.TextField(null=True)
    
    def __str__(self):
        """ 
        Cette méthode décrit le métier que pratique l'entreprise dans son secteur d'activité.
        """
        return self.libelle_meti


class Forme_Juri(models.Model):
    libelle_juri = models.CharField(max_length=42)		# Nom de la forme juridique
    description_juri = models.TextField(null=True)
    
    def __str__(self):
        """ 
        Cette méthode décrit la forme juridique de l'entreprise : SA (Société Anonime), SARL (Société A Responsabilité Limitée), ....
        """
        return self.libelle_juri

class Adresse_Post(models.Model):
    numero_et_rue = models.CharField(max_length=100)		# Numéro et nom de rue
    appart_bati = models.CharField(max_length=42, null=True)	# Numéro appartement et batiment
    boite_postale = models.CharField(max_length=42, null=True)	# Boite postale
    code_postal_commune = models.CharField(max_length=110,
                       default="81000 Albi")            	# Code postal
    
    def __str__(self):
        """ 
        Cette méthode décrit tous les contacts de l'entreprise
        """
        return self.numero_et_rue+" "+self.code_postal_commune

        
class Evenement(models.Model):
    titre_evt = models.CharField(max_length=100, null=True)	# Le titre de l'événement
    resume_evt = models.CharField(max_length=200, null=True)	# Résumé de l'évènement
    date_evt = models.DateTimeField(auto_now=False, 
                                verbose_name="Date de l'événement", null=True)
    detail_evt = models.TextField(null=True)                    # Détail de l'évènement
    
    def __str__(self):
        """ 
        Cette méthode décrit tous les contacts de l'entreprise
        """
        return self.titre_evt

class Respon_Boite(models.Model):
    nom_resp = models.CharField(max_length=42)			# Nom du responsable
    prenom_resp = models.CharField(max_length=42)		# prénom du responsable
    titre_resp = models.CharField(max_length=42)		# Titre du responsable: DG, PDG, Gérant, ...
    tel_resp = models.CharField(max_length=100)			# Téléphone portable et/ou fixe
    mail_resp = models.CharField(max_length=100, null=True)	# Téléphone portable et/ou fixe
    
    def __str__(self):
        """ 
        Cette méthode décrit l'adresse postale de l'entreprise
        """
        return self.prenom_resp+" "+self.nom_resp
#        return self.nom_resp
        
                
        
class Entreprise(models.Model):
    raison_sociale = models.CharField(max_length=42)
    secteur_activite = models.ForeignKey('Secteur_Activ')	# Liaison avec le modèle Secteur_Activ 
    metier_ent = models.ForeignKey('Metier_Activ')		# Liaison avec le modèle Metier_Activ 
    logo = models.ImageField(upload_to="logos/", null=True)     # Dossier des logos
    image = models.ImageField(upload_to="photos/", null=True)   # Dossier des logos
    
    forme_juridique = models.ForeignKey('Forme_Juri')		# Liaison avec le modèle Forme_Juri
    adresse_postale = models.ForeignKey('Adresse_Post', null=True)		# Liaison avec le modèle Adresse_Post
    telephone = models.CharField(max_length=15, null=True)
    fax = models.CharField(max_length=15, null=True)
    responsable = models.ForeignKey('Respon_Boite')		# Liaison avec le modèle Respon_Boite
    date_creation = models.DateTimeField(auto_now=False, 
                                verbose_name="Date de creation", null=True)
    description_resume = models.TextField(null=True)
    description = models.TextField(null=True)
    registre_commerce = models.CharField(max_length=42)
    adresse_mail = models.CharField(max_length=81)
    site_web = models.CharField(max_length=100, null=True)
    
    evenement_entr = models.ForeignKey('Evenement', null=True)		# Evénement de l'entreprise
   
    def __str__(self):
        """ 
        Cette méthode présente l'entreprise dans toute sa complexité
        """
        return self.raison_sociale