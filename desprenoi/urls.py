from django.urls import path

from desprenoi import views

urlpatterns = [
    path('despre_noi/', views.DesprenoiTemplateView.as_view(), name='despre-noi'),
]