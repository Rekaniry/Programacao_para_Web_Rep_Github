from django.shortcuts import render
from django.views.generic.base import View
from django.http.response import HttpResponseRedirect
from django.urls.base import reverse_lazy

class ContatoCreateView(View):
    def get(self, request, *args, **kwargs):
        contexto = { 'formulario': ContatoModel2Form, }

        return render(request, "contatos/criaContato.html", contexto)

    def post(self, request, *args, **kwargs):
        formulario = ContatoModel2Form(request.POST)

        if formulario.is_valid():
            contato = formulario.save()
            contato.save()

        return HttpResponseRedirect(reverse_lazy("contatos:lista-contatos"))

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
    dtNasc = forms.DateField(
        input_formats=['%d/%m/%Y'],
        label='Data do nascimento',
        help_text='Nascimento no formato DD/MM/AAAA',
    )

class Meta:
    model = Pessoa
    fields = '__all__'