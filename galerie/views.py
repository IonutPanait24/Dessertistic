from django.shortcuts import render
from django.views.generic import TemplateView

class GalerieTemplateView(TemplateView):
    template_name = 'galerie/galerie.html'
