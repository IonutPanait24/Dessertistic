from django.shortcuts import render
from django.views.generic import TemplateView


class DesprenoiTemplateView(TemplateView):
    template_name = 'desprenoi/desprenoi.html'


