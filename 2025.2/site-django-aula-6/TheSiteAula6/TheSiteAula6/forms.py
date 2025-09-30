from django import forms

class ExemploForm(forms.Form):
    campoBooleanField = forms.BooleanField(
        required=True,
        label='Campo BooleanField',
        label_suffix='*:',
        help_text='Marque esta caixa se você concorda.',
        initial=False,
        error_messages={
            'required': 'Você deve concordar para continuar.'
        },
        widget=forms.CheckboxInput(
            attrs={
                'class': 'classe-booleanfield'
            }
        )
    )

    campoCharField = forms.CharField(
        required=True,
        label='Campo CharField',
        label_suffix='*:',
        max_length=100,
        help_text='Digite um texto de até 100 caracteres.',
        initial='Texto inicial',
        error_messages={
            'required': 'Campo necessário'
        },
        widget=forms.TextInput(
            attrs={
                'class': 'classe-charfield',
                'placeholder': 'Digite algo aqui...'
            }
        )
    )

    campoBusca = forms.CharField(
        required=True,
        label="Campo busca",
        label_suffix=": ",
        help_text="Entre uma busca",
        error_messages = {
            'required': 'Campo necessário',
            'invalid': "Campo busca inválido",
        },
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'classeBusca',
                'type': 'search',
            }
        ),
    )

    campoTelefone = forms.CharField(
        required=True,
        label="Campo telefone",
        label_suffix=": ",
        initial="555-123-1234",
        help_text="Entre um telefone",
        error_messages = {
            'required': 'Esse campo é necessário',
            'invalid': "Campo telefone inválido",
        },
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'classeTelefone',
                'type': 'tel',
                'pattern': "[0-9]{3}-[0-9]{3}-[0-9]{4}",
            }
        ),
    )

    campoSenha = forms.CharField(
        required=True,
        label="Campo senha",
        label_suffix=": ",
        help_text="Entre uma senha",
        error_messages = {
            'required': 'Campo necessário',
            'invalid': "Campo senha inválido",
        },
        max_length=100,
        widget=forms.PasswordInput(
            attrs={
                'class': 'classeSenha',
            }
        )
    )

    campoDecimal = forms.DecimalField(
        required=True,
        label="Campo decimal",
        label_suffix=": ",
        initial="87.52",
        help_text="Entre um número real",
        error_messages = {
            'required': 'Campo necessário',
            'invalid': "Campo decimal inválido",
        },
        disabled=False,
        widget=forms.NumberInput(
            attrs={
                'class': 'classeNumeroReal',
                'min': '-15', 'max': '100', 'step': '0.2',
            }
        ),
        max_digits=5,
        decimal_places=3,
    )

    campoInteiro = forms.IntegerField(
        required=True,
        label="Campo número",
        label_suffix=": ",
        initial="8752",
        help_text="Entre um número inteiro",
        error_messages = {
            'required': 'Campo necessário',
            'invalid': "Campo inteiro inválido",
        },
        disabled=False,
        widget=forms.NumberInput(
            attrs={
                'class': 'classeNumero',
                'min': '-15', 'max': '100', 'step': '10',
            }
        ),
    )

    campoFaixa = forms.IntegerField(
        required=True,
        label="Campo faixa",
        label_suffix=": ",
        initial="8752",
        help_text="Selecione um valor",
        error_messages = {
            'required': 'Esse campo faixa é necessário',
            'invalid': "Campo faixa inválido",
        },
        disabled=False,
        widget=forms.NumberInput(
            attrs={
                'class': 'classeFaixa',
                'type': 'range',
                'min': '-15', 'max': '100', 'step': '10',
            }
        ),
    )

    campoArea = forms.CharField(
        required=True,
        label="Campo área",
        label_suffix=": ",
        initial=
            "Exemplo de campo área.\n" +
            "O texto pode ter várias linhas.",
        help_text="Entre um texto com várias linhas",
        error_messages = {
            'required': 'Esse campo área é necessário',
            'invalid': "Campo área inválido",
        },
        max_length=100,
        widget=forms.Textarea(
            attrs={
                'class': 'classeArea',
                'cols': 40, 'rows': 10,
            }
        ),
    )

    campoRadio = forms.ChoiceField(
        required=True,
        label="Campo rádio",
        label_suffix=": ",
        initial="opcao2",
        help_text="Escolha uma opção",
        error_messages = {
            'required': 'Campo necessário',
            'invalid': "Campo rádio inválido",
        },
        choices=[
            ('opcao1','opcao 1'),
            ('opcao2','opcao 2'),
            ('opcao3','opcao 3'),
            ('opcao4','opcao 4'),
        ],
        widget=forms.RadioSelect(
            attrs={
                'class': 'classeRadio',
            }
        ),
    )

    campoSelect = forms.ChoiceField(
        required=True,
        label="Campo select",
        label_suffix=": ",
        initial="opcao3",
        help_text="Escolha uma opção",
        error_messages = {
            'required': 'Campo necessário',
            'invalid': "Campo select inválido",
        },
        choices=[
            ('opcao1','opcao 1'),
            ('opcao2','opcao 2'),
            ('opcao3','opcao 3'),
            ('opcao4','opcao 4'),
        ],
        widget=forms.Select(
            attrs={
                'class': 'classeSelect'
            }
        ),
    )

    campoSelectMultiplo = forms.ChoiceField(
        required=True,
        label="Campo select multiplo",
        label_suffix=": ",
        initial=["opcao2","opcao3"],
        help_text="Escolha várias opções",
        error_messages = {
            'required': 'Campo necessário',
            'invalid': "Campo inválido",
        },
        choices=[
            ('opcao1','opcao 1'),
            ('opcao2','opcao 2'),
            ('opcao3','opcao 3'),
            ('opcao4','opcao 4'),
        ],
        widget=forms.Select(
            attrs={
                'class': 'classeSelect',
                'multiple': 'multiple',
            }
        ),
    )

    campoCheckbox = forms.ChoiceField(
        required=True,
        label="Campo checkbox",
        label_suffix=": ",
        initial=["opcao1","opcao3"],
        help_text="Escolha uma opção",
        error_messages = {
            'required': 'Esse campo checkbox é necessário',
            'invalid': "Campo checkbox inválido",
        },
        choices=[
            ('opcao1','opcao 1'),
            ('opcao2','opcao 2'),
            ('opcao3','opcao 3'),
            ('opcao4','opcao 4'),
        ],
        widget=forms.CheckboxSelectMultiple(
            attrs={
                'class': 'classeSelectMultiplo',
            }
        ),
    )

    campoCor = forms.CharField(
        required=True,
        label='Campo cor',
        label_suffix=": ",
        initial='#FF0000',
        help_text='Escolha uma cor',
        error_messages = {
            'required': 'Campo necessário',
            'invalid': "Campo cor inválido",
        },
        widget=forms.TextInput(
            attrs={
                'class': 'classeCor',
                'type': 'color'
            }
        ),
    )

    campoData = forms.DateField(
        required=True,
        label="Campo data",
        label_suffix=": ",
        initial='1970-01-02',
        help_text="Entre uma data",
        error_messages = {
            'required': 'Esse campo data é necessário',
            'invalid': "Campo data inválido",
        },
        disabled=False,
        widget=forms.SelectDateWidget(
            attrs={
                'class': 'classeData',
            },
            years=[_ for _ in range(1900, 2100)]
        ),
    )

    campoDataPicker = forms.DateField(
        required=True,
        label="Campo data picker",
        label_suffix=": ",
        initial='1970-01-02',
        help_text="Entre uma data",
        error_messages = {
            'required': 'Campo necessário',
            'invalid': "Campo inválido",
        },
        disabled=False,
        widget=forms.DateInput(
            attrs={
                'class': 'classeDataPicker',
                'type': 'date',
            },
        ),
    )

    campoEmail = forms.EmailField(
        required=True,
        label="Campo email",
        label_suffix=": ",
        initial="felipefalcao2910@gmail.com",
        help_text="Entre um endereço de email",
        error_messages = {
            'required': 'Campo necessário',
            'invalid': "Campo email inválido",
        },
        disabled=False,
        max_length=100,
        widget=forms.EmailInput(
            attrs={
                'class': 'classeEmail',
            },
        )
    )

    campoURL = forms.URLField(
        required=True,
        label="Campo URL",
        label_suffix=": ",
        initial="google.com",
        help_text="Entre uma URL",
        error_messages = {
            'required': 'Esse campo URL é necessário',
            'invalid': "Campo URL inválido",
        },
        disabled=False,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'classeURL',
            }
        ),
    )

    campoArquivo = forms.FileField(
        required=True,
        label="Campo arquivo",
        label_suffix=": ",
        initial="Exemplo de campo arquivo",
        help_text="Selecione um arquivo",
        error_messages = {
            'required': 'Campo necessário',
            'invalid': "Campo arquivo inválido",
        },
        disabled=False,
        max_length=100,
        widget=forms.ClearableFileInput(
            attrs={
                'class': 'classeEmail',
            }
        ),
    )
