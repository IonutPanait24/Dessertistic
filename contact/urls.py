from django.urls import path

from contact import views

urlpatterns = [
    path('contact', views.ContactTemplateView.as_view(), name='contact-me'),
]