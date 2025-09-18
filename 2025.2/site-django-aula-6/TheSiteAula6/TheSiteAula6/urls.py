from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from TheSiteAula6 import views

urlpatterns = [
    path("", views.home_page_pagina, name='home-page-pagina'),
    path("admin/", admin.site.urls, name='admin'),
    path("Contatos/", include('Contatos.urls')),
    # links para segurança
    path("seguranca/", views.homeSec, name='home-sec'),
    path('seguranca/registro/', views.registro, name='registro'), 
]
