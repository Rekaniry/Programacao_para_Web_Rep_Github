from django.shortcuts import render
from Contatos.models import Pessoa, Endereco
from django.views.generic.base import View
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy

def home_page_pagina(request):
    return render(request, 'Contatos/index.html')

def home_page_contatos(request):
    return render(request, 'Contatos/home_page_contatos.html')

class ContatoCreateView(View):
    '''
    Classe para criar um novo contato.
    '''
    def get(self, request, *args, **kwargs):
        '''
        Exibe o formulário para criar um novo contato.
        '''
        contexto = {
            'formulario': ContatoModel2Form,
            'enderecos': EnderecosModel2Form,
            'titulo_janela': 'Cria Contato',
            'titulo_pagina': 'Cria Contato',
            'botao': 'Criar contato',
        }

        return render(request, "Contatos/formContato.html", contexto)
    
    def post(self, request, *args, **kwargs):
        '''
        Cria um novo contato.
        '''
        formulario = ContatoModel2Form(request.POST)
        enderecos = EnderecosModel2Form(request.POST)

        if formulario.is_valid():
            # Salva o formulário
            formulario.save()
            
            # Obtém o valor do campo 'nome' do formulário de contato
            endereco_referente_a_pessoa = formulario.cleaned_data['nome']
            
            # Verifica se há exatamente uma pessoa com o nome fornecido
            pessoas = Pessoa.objects.filter(nome=endereco_referente_a_pessoa)
            
            if pessoas.count() != 1:
                contexto = {
                    'formulario': formulario,
                    'enderecos': enderecos,
                    'mensagem': 'Já existe mais de um contato com esse nome. Por favor, utilize nomes únicos para os contatos.',
                    'titulo_janela': 'Cria Contato',
                    'titulo_pagina': 'Cria Contato',
                    'botao': 'Criar contato',
                }

                return render(request, "Contatos/formContato.html", contexto)

            # Associa a instância de Pessoa ao formulário de endereços
            enderecos.instance.pessoa = endereco_referente_a_pessoa
            
            if enderecos.is_valid():
                # Salva o formulário de endereços
                enderecos.save()
                
                contexto = {
                    'formulario': ContatoModel2Form(),
                    'enderecos': EnderecosModel2Form(),
                    'mensagem': 'Contato criado com sucesso!',
                    'titulo_janela': 'Cria Contato',
                    'titulo_pagina': 'Cria Contato',
                    'botao': 'Criar contato',
                }
    
                return HttpResponseRedirect(reverse_lazy("Contatos:lista-contatos"))
        else:
            contexto = {
                'formulario': formulario,
                'enderecos': enderecos,
                'mensagem': 'Erro ao criar contato. Verifique os dados informados.',
                'titulo_janela': 'Cria Contato',
                'titulo_pagina': 'Cria Contato',
                'botao': 'Criar contato',
            }
            return render(request, "Contatos/formContato.html", contexto)

class ContatoUpdateView(View):
    '''
    Classe para atualizar um contato.
    '''
    def get(self, request, pk, *args, **kwargs):
        '''
        Exibe o formulário para atualizar um contato.
        '''
        pessoa = Pessoa.objects.get(pk=pk)
        formulario = ContatoModel2Form(instance=pessoa)
        enderecos = EnderecosModel2Form(instance=pessoa.enderecos.first())
        contexto = {
            'formulario': formulario,
            'enderecos': enderecos,
            'titulo_pagina': 'Atualiza Contato',
            'titulo_janela': 'Atualiza Contato',
            'botao': 'Atualizar',
        }

        return render(request, "Contatos/formContato.html", contexto)
    
    def post(self, request, pk, *args, **kwargs):
        '''
        Atualiza o contato.
        '''
        pessoa = Pessoa.objects.get(pk=pk)
        formulario = ContatoModel2Form(request.POST, instance=pessoa)
        enderecos = EnderecosModel2Form(request.POST, instance=pessoa.enderecos.first())

        if formulario.is_valid() and enderecos.is_valid():
            formulario.save()

            endereco_referente_a_pessoa = formulario.cleaned_data['nome']
            
            pessoas = Pessoa.objects.filter(nome=endereco_referente_a_pessoa)

            enderecos.instance.pessoa = pessoa

            if enderecos.is_valid():
                enderecos.save()

            return HttpResponseRedirect(reverse_lazy("Contatos:lista-contatos"))
        else:
            contexto = {
                'formulario': formulario,
                'mensagem': 'Erro ao atualizar contato. Verifique os dados informados.',
                'janela_titulo': 'Atualiza Contato',
                'janela_pagina': 'Atualiza Contato',
                'botao': 'Atualizar',
            }
            return render(request, "Contatos/formContato.html", contexto)

class ContatoDeleteView(View):
    '''
    Classe para deletar um contato.
    '''
    def get(self, request, pk, *args, **kwargs):
        '''
        Exibe uma página de confirmação para deletar o contato.
        '''
        pessoa = Pessoa.objects.get(pk=pk)
        # Caso não queira mostrar os dados do formulário
        # contexto = { 'pessoa': pessoa, }
        # Caso queira mostrar os dados do formulário
        formulario = ContatoModel2Form(instance=pessoa)
        enderecos = EnderecosModel2Form(instance=pessoa.enderecos.first())
        contexto = {
            'formulario': formulario,
            'enderecos': enderecos,
            'titulo_janela': 'Deleta Contato',
            'titulo_pagina': 'Deleta Contato',
            'botao': 'Excluir',
        }

        return render(request, "Contatos/formContato.html", contexto)
    
    def post(self, request, pk, *args, **kwargs):
        '''
        Apaga o contato
        '''
        pessoa = Pessoa.objects.get(pk=pk)
        pessoa.delete()

        return HttpResponseRedirect(reverse_lazy("Contatos:lista-contatos"))

class ContatoListView(View):
    '''
    Classe para listar contatos.
    '''
    def get(self, request, *args, **kwargs):
        # Recupera todas as pessoas com endereços pré-carregados
        pessoas = Pessoa.objects.all().order_by('nome').prefetch_related('enderecos')
        
        # Cria o atributo dinâmico (não recomendado, mas funcional)
        for pessoa in pessoas:
            pessoa.enderecos_list = pessoa.enderecos.all()

        # Contexto para o template
        # Valor da chave é o objeto com todas as pessoas = { Chave 'pessoas': Dicionário contexto }
        contexto = {
            'pessoas': pessoas,
        }

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

class EnderecosModel2Form(forms.ModelForm):
    class Meta:
        model = Endereco
        fields = [
            'logradouro',
            'numero',
            'complemento',
            'bairro',
            'cidade',
            'estado',
            'cep',
        ]
        labels = {
            'logradouro': 'Logradouro',
            'numero': 'Número',
            'complemento': 'Complemento',
            'bairro': 'Bairro',
            'cidade': 'Cidade',
            'estado': 'Estado (UF)',
            'cep': 'CEP',
        }
        help_texts = {
            'logradouro': 'Informe o logradouro do endereço.',
            'numero': 'Informe o número do endereço.',
            'complemento': 'Informe o complemento do endereço (opcional).',
            'bairro': 'Informe o bairro do endereço.',
            'cidade': 'Informe a cidade do endereço.',
            'estado': 'Informe o estado (UF) do endereço.',
            'cep': 'Informe o CEP do endereço.',
        }
        error_messages = {
            'logradouro': {
                'max_length': 'O logradouro é muito grande.',
                'required': 'O logradouro é obrigatório.',
            },
            'numero': {
                'max_length': 'O número é muito grande.',
                'required': 'O número é obrigatório.',
            },
            'complemento': {
                'max_length': 'O complemento é muito grande.',
            },
            'bairro': {
                'max_length': 'O bairro é muito grande.',
                'required': 'O bairro é obrigatório.',
            },
            'cidade': {
                'max_length': 'A cidade é muito grande.',
                'required': 	'A cidade é obrigatória.',
            },
            'estado': {
                'max_length': 	'O estado (UF) é muito grande.',
               	'required': 	'O estado (UF) é obrigatório.',
            },
           	'cep': {
               	'max_length': 	'O CEP é muito grande.',
               	'required': 	'O CEP é obrigatório.',
            	},
        	}