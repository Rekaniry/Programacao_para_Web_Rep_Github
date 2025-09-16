from django.db import models

class Pessoa(models.Model):
    id = models.AutoField(primary_key = True)
    nome = models.CharField(
        max_length = 100,
        help_text = 'Entre o nome'
    )
    idade = models.IntegerField(help_text = 'Entre a idade')
    salario = models.DecimalField(
        help_text = 'Entre o salário',
        decimal_places = 2,
        max_digits = 8
    )
    email = models.EmailField(
        help_text = 'Informe o email',
        max_length = 254
    )
    telefone = models.CharField(
        help_text = 'Telefone com DDD e DDI',
        max_length = 20
    )
    data_nascimento = models.DateField(
        help_text = 'Nascimento no formato DD/MM/AAAA',
        verbose_name = 'Data de nascimento'
    )

    def __str__(self):
        return self.nome

class Endereco(models.Model):
    '''
    Modelo que representa um endereço associado a uma pessoa.
    '''

    id = models.AutoField(primary_key=True)

    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE, related_name='enderecos')
    logradouro = models.CharField(max_length=200, help_text='Logradouro do endereço')
    numero = models.CharField(max_length=10, help_text='Número do endereço')
    complemento = models.CharField(max_length=100, blank=True, help_text='Complemento do endereço (opcional)')
    bairro = models.CharField(max_length=100, help_text='Bairro do endereço')
    cidade = models.CharField(max_length=100, help_text='Cidade do endereço')
    estado = models.CharField(max_length=2, help_text='Estado (UF) do endereço')
    cep = models.CharField(max_length=10, help_text='CEP do endereço')

    def __str__(self):
        return f"{self.pessoa}: {self.logradouro}, {self.numero} - {self.cidade}/{self.estado} - CEP: {self.cep}"
    