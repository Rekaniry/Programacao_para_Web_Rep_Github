from django.shortcuts import render
from Contatos.models import Pessoa
from django.views.generic.base import View
from django import forms

def home_page_pagina(request):
    return render(request, 'Contatos/index.html')

def home_page_contatos(request):
    return render(request, 'Contatos/home_page_contatos.html')

class ContatoCreateView(View):
    def get(self, request, *args, **kwargs):
        contexto = { 'formulario': ContatoModel2Form, }

        return render(request, "Contatos/criaContato.html", contexto)

    def post(self, request, *args, **kwargs):
        formulario = ContatoModel2Form(request.POST)

        if formulario.is_valid():
            contato = formulario.save()
            contato.save()

        # return HttpResponseRedirect(reverse_lazy("Contatos:lista-contatos"))
        # OU
        contexto = { 'formulario': formulario, }
        return render(request, "Contatos/criaContato.html", contexto)

class ContatoListView(View):
    def get(self, request, *args, **kwargs):
        # Recupera todas as pessoas do banco de dados
        pessoas = Pessoa.objects.all().order_by('nome')

        # Contexto para o template
        # Valor da chave é o objeto com todas as pessoas = { Chave 'pessoas': Dicionário contexto }
        contexto = { 'pessoas': pessoas, }

        return render(
            request,
            'Contatos/listaContatos.html',
            contexto
        )

class ContatoModel2Form(forms.ModelForm):
    class Meta:
        model = Pessoa
        fields = '__all__'
        fields = [
            'nome',
            'idade',
            'salario',
            'email',
            'telefone',
            'data_nascimento',
        ]
        labels = {
            'nome': 'Nome completo',
            'idade': 'Idade (em anos)',
            'salario': 'Salário (em R$) (Ex: 3500.00)',
            'email': 'E-mail (Ex: usuario@exemplo.com)',
            'telefone': 'Telefone (DDD) + Número (Ex: 21999999999)',
            'data_nascimento': 'Data de nascimento (DD/MM/AAAA)',
        }
        help_texts = {  
            'nome': 'Informe o nome completo da pessoa.',
            'idade': 'Informe a idade em anos.',
            'salario': 'Informe o salário em Reais.',
            'email': 'Informe um e-mail válido.',
            'telefone': 'Informe o telefone com DDD.',
            'data_nascimento': 'Informe a data no formato DD/MM/AAAA.',
        }
        error_messages = {
            'nome': {
                'max_length': 'O nome é muito grande.',
                'required': 'O nome é obrigatório.',
            },
            'idade': {
                'invalid': 'Informe um número inteiro válido para a idade.',
                'required': 'A idade é obrigatória.',
            },
            'salario': {
                'invalid': 'Informe um número válido para o salário.',
                'required': 'O salário é obrigatório.',
            },
            'email': {
                'invalid': 'Informe um e-mail válido.',
                'required': 'O e-mail é obrigatório.',
            },
            'telefone': {
                'invalid': 'Informe um telefone válido.',
                'required': 'O telefone é obrigatório.',
            },
            'data_nascimento': {
                'invalid': 'Informe uma data válida no formato DD/MM/AAAA.',
                'required': 'A data de nascimento é obrigatória.',
            },
        }