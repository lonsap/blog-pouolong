#-*- coding: utf-8 -*-
from django.shortcuts import render
from datetime import datetime

from django.http import HttpResponse

from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from datetime import datetime
from .models import Entreprise, Respon_Boite, Adresse_Post, Forme_Juri, Metier_Activ, Secteur_Activ, Evenement
from .forms import Secteur_ActivForm, Metier_ActivForm, Forme_JuriForm, Adresse_PostForm, Respon_BoiteForm, EntrepriseForm, EvenementForm



def entr_list(request):
    """ Point d'entrée du site """
    entrs = Entreprise.objects.all().order_by('date_creation')
    return render(request, 'boite/entr_list.html', {'entrs': entrs, 'date': datetime.now()})
#    return render(request, 'boite/base.html', {'date': datetime.now()})

def entr_list_0(request):
    entrs = Entreprise.objects.all().order_by('date_creation')
#    entrs = Entreprise.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'boite/entr_list.html', {'entrs': entrs, 'date': datetime.now()})
    
def entr_detail(request, pk):
    entr = get_object_or_404(Entreprise, pk=pk)
    return render(request, 'boite/entr_detail.html', {'entr': entr, 'date': datetime.now()})
    
def entr_new(request):
    if request.method == "POST":
        form = EntrepriseForm(request.POST)
        if form.is_valid():
            entr = form.save(commit=False)
            entr.responsable = request.user
            entr.date_creation = timezone.now()
            entr.save()
            return redirect('boite.views.entr_detail', pk=entr.pk)
    else:
        form = EntrepriseForm()
    return render(request, 'boite/entr_edit.html', {'form': form})
    
def entr_edit(request, pk):
    entr = get_object_or_404(Entreprise, pk=pk)
    if request.method == "POST":
        form = EntrepriseForm(request.POST, instance=entr)
        if form.is_valid():
            entr = form.save(commit=False)
            entr.responsable = request.user
            entr.date_creation = timezone.now()
            entr.save()
            return redirect('boite.views.entr_detail', pk=entr.pk)
    else:
        form = EntrepriseForm(instance=entr)
    return render(request, 'boite/entr_edit.html', {'form': form})