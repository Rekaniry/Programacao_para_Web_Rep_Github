from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from TheSiteAula6 import views
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.views import PasswordChangeDoneView
from django.views.generic.edit import UpdateView
from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView
from django.contrib.auth.views import PasswordResetConfirmView, PasswordResetCompleteView

urlpatterns = [
    path(
        "", 
        views.home_page_pagina, 
        name='home-page-pagina'
    ),
    
    path(
        "admin/", 
        admin.site.urls, 
        name='admin'
    ),
    
    path(
        "Contatos/", 
        include('Contatos.urls')
    ),
    
    path(
        "seguranca/", 
        views.homeSec, 
        name='home-sec'
    ),
    
    path(
        'seguranca/registro/', 
        views.registro, 
        name='registro'
    ),
    
    path(
        'seguranca/login/', 
        LoginView.as_view(
            template_name='seguranca/login.html'
        ), 
        name='login'
    ),
    
    path(
        'accounts/login/', 
        LoginView.as_view(
            template_name='seguranca/login.html'
        ), 
        name='login'
    ),
    
    path(
        'privado/paginaSecreta/', 
        views.paginaSecreta, 
        name='paginaSecreta'
    ),
    
    path(
        'meulogout/', 
        views.logout, 
        name='meulogout'
    ),
    
    path(
        'logout/', 
        LogoutView.as_view(
            next_page=reverse_lazy('home-sec')
        ), 
        name='logout'
    ),
    
    path(
        'seguranca/password_change_form/', 
        PasswordChangeView.as_view(
            template_name='seguranca/password_change_form.html', 
            success_url=reverse_lazy('password_change_done')
        ), 
        name='password_change_form'
    ),
    
    path(
        'seguranca/password_change_done/', 
        PasswordChangeDoneView.as_view(
            template_name='seguranca/password_change_done.html'
        ), 
        name='password_change_done'
    ),
    
    path(
        'seguranca/editarPerfil/<int:pk>/', 
        UpdateView.as_view(
            template_name='seguranca/user_form.html', 
            success_url=reverse_lazy('home-sec'), 
            model=User, 
            fields=['first_name', 'last_name', 'email']
        ), 
        name='editarPerfil'
    ),

    path(
        'seguranca/password_reset/', 
        PasswordResetView.as_view(
            template_name='seguranca/password_reset_form.html',
            success_url=reverse_lazy('password_reset_done'),
            html_email_template_name='seguranca/password_reset_email.html',
            subject_template_name='seguranca/password_reset_subject.txt',
            from_email='webmaster@yss.com.br',
        ), 
        name='password_reset'
    ),
    
    path(
        'seguranca/password_reset_done/', 
        PasswordResetDoneView.as_view(
            template_name='seguranca/password_reset_done.html',
        ), 
        name='password_reset_done'
    ),
    
    path(
        'seguranca/password_reset_confirm/<uidb64>/<token>/',
        PasswordResetConfirmView.as_view(
            template_name='seguranca/password_reset_confirm.html',
            success_url=reverse_lazy('password_reset_complete'),
        ), 
        name='password_reset_confirm'
    ),
    
    path(
        'seguranca/password_reset_complete/', 
        PasswordResetCompleteView.as_view(
            template_name='seguranca/password_reset_complete.html'
        ), 
        name='password_reset_complete'
    )
]
