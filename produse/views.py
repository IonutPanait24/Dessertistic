from django.shortcuts import render
from django.views.generic import TemplateView





class TorturiTemplateView(TemplateView):
    template_name = 'produse/torturi.html'


class TorturiPersonalizateTemplateView(TemplateView):
    template_name = 'produse/torturi_personalizate.html'

class PatiserieTemplateView(TemplateView):
    template_name = 'produse/patiserie.html'

class MiniPrajituriTemplateView(TemplateView):
    template_name = 'produse/mini_prajituri.html'
