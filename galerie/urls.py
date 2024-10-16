from django.urls import path

from galerie import views

urlpatterns = [
    path("galerie/", views.GalerieTemplateView.as_view(), name="galerie-produse"),
]