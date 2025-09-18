from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm

def home_page_pagina(request):
    '''
    Renderiza a página inicial do site.
    '''
    return render(request, 'TheSiteAula6/home.html')

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