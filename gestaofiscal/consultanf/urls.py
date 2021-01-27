from django.urls import path
from consultanf import views

urlpatterns = [
    path('', views.index, name='index'),
    path('NotaFiscal/')
]