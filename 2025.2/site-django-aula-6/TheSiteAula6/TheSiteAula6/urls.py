from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from TheSiteAula6 import views
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.views import PasswordChangeDoneView

urlpatterns = [
    path("", views.home_page_pagina, name='home-page-pagina'),
    path("admin/", admin.site.urls, name='admin'),
    path("Contatos/", include('Contatos.urls')),
    path("seguranca/", views.homeSec, name='home-sec'),
    path('seguranca/registro/', views.registro, name='registro'),
    path('seguranca/login/', LoginView.as_view(template_name='seguranca/login.html'), name='login'),
    path('accounts/login/', LoginView.as_view(template_name='seguranca/login.html'), name='login'),
    path('privado/paginaSecreta/', views.paginaSecreta, name='paginaSecreta'),
    path('meulogout/', views.logout, name='meulogout'),
    path('logout/', LogoutView.as_view(next_page=reverse_lazy('home-sec')), name='logout'),
    path('seguranca/password_change_form/', PasswordChangeView.as_view(template_name='seguranca/password_change_form.html', success_url=reverse_lazy('password_change_done')), name='password_change_form'),
    path('seguranca/password_change/done/', PasswordChangeDoneView.as_view(template_name='seguranca/password_change_done.html'), name='password_change_done'),
]
