from django.db import models

# Create your models here.
from django.db import models
        
        
class My_contact(models.Model):
    numero_rue = models.CharField(max_length=255)
    code_postal = models.CharField(max_length=6)
    commune = models.CharField(max_length=255)
    telephone = models.CharField(max_length=20)
    adr_mail = models.CharField(max_length=50)
    # carte = models.ImageField(upload_to="")
    
    def __str__(self):
           return self.telephone

class My_menus(models.Model):
    langue = models.CharField(max_length=200)
    # author = models.ForeignKey('auth.User')
    menu_blog = models.CharField(max_length=200)
    menu_lst_boite = models.CharField(max_length=200)      # Liste des entreprises
    menu_faq = models.CharField(max_length=200)
    menu_news = models.CharField(max_length=200)           # Nouvelles
    menu_contacts = models.ForeignKey('My_contact')        # Nos contacts

    def publish(self):
        self.langue = "fr"
        self.save()

    def __str__(self):
        return self.langue
