from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from Contatos import views

urlpatterns = [
    path('', views.home_page_pagina, name='home-page-pagina'),
    path("admin/", admin.site.urls),
    path("Contatos/", include('Contatos.urls')),
]
