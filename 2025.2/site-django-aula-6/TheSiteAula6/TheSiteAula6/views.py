from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from TheSiteAula6.forms import ExemploForm

def home_page_pagina(request):
    '''
    Renderiza a página inicial do site.
    '''
    return render(request, 'TheSiteAula6/home.html')

def exemplo_form(request):
    '''
    Renderiza um formulário de exemplo.
    '''
    if request.method == 'POST':
        pass
    else:
        formulario = ExemploForm()
    
    contexto = {'form': formulario, }
    return render(request, 'TheSiteAula6/exemplo_form.html', contexto)

def homeSec(request):
    '''
    Renderiza a página
    '''
    return render(request, 'seguranca/homeSec.html')

def registro(request):
    '''
    Renderiza a página de registro de usuários.
    '''
    
    if request.method == 'POST':
        formulario = UserCreationForm(request.POST)
        
        if formulario.is_valid():
            formulario.save()
        
        return redirect('home-sec')
    else:
        formulario = UserCreationForm()
    
    context = {'form': formulario, }
    
    return render(request, 'seguranca/registro.html', context)

@login_required
def paginaSecreta(request):
    '''
    Renderiza uma página secreta que querer autenticação.
    '''

    return render(request, 'privado/paginaSecreta.html')

def logout(request):
    '''
    Renderiza a página de logout.
    '''

    return render(request, 'seguranca/logout.html')
