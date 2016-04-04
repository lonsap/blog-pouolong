from django import forms
from django.forms import ModelForm

from .models import Entreprise, Respon_Boite, Adresse_Post, Forme_Juri, Metier_Activ, Secteur_Activ, Evenement

class Secteur_ActivForm(forms.ModelForm):
    class Meta:
        model = Secteur_Activ
        fields = '__all__'

class Metier_ActivForm(forms.ModelForm):
    class Meta:
        model = Metier_Activ
        fields = '__all__'

class Forme_JuriForm(forms.ModelForm):
    class Meta:
        model = Forme_Juri
        fields = '__all__'

class Adresse_PostForm(forms.ModelForm):
    class Meta:
        model = Adresse_Post
        fields = '__all__'


class Respon_BoiteForm(forms.ModelForm):
    class Meta:
        model = Respon_Boite
        fields = '__all__'

class EntrepriseForm(forms.ModelForm):
    class Meta:
        model = Entreprise
        fields = '__all__'

class EvenementForm(forms.ModelForm):
    class Meta:
        model = Evenement
        fields = '__all__'
