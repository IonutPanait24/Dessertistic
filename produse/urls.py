from django.urls import path

from produse import views

urlpatterns = [
    path('torturi/', views.TorturiTemplateView.as_view(), name='torturi'),
    path('torturi_personalizate/', views.TorturiPersonalizateTemplateView.as_view(), name='torturi-personalizate'),
    path('mini_prajituri/', views.MiniPrajituriTemplateView.as_view(), name='mini-prajituri'),
    path('patiserie/', views.PatiserieTemplateView.as_view(), name='patiserie'),
]