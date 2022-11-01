from email.policy import default
from logging import PlaceHolder
from django import forms
from django.forms import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

def solo_caracteres(valor):
    if any(char.isdigit() for char in valor):
        raise ValidationError('Error al ingresar números: %(valor)s',code='Error1',params={'valor':valor})
'''se podrían discriminar otros dígitos

opciones_asunto = [
    (1, 'Consulta'),
    (2, 'Reclamo'), 
    (3, 'Sugerencia'), 
    (4, 'Felicitaciones'),
    (5, 'Otros')
]'''

class ContactoForm(forms.Form):

    nombre = forms.CharField(
        label='Nombre',
        max_length=50,
        error_messages={
           'required':'Por favor, ingrese el nombre'
        },
        validators=(solo_caracteres,),
        widget=forms.TextInput(attrs={'class':'form-control'})
        )

    email = forms.EmailField(
        label='Email',
        max_length=150,
        error_messages={
           'required':'Por favor, ingrese el email'
        },
        widget=forms.TextInput(attrs={'class':'form-control','type':'email','placeholder':'info@gmail.com'})
        )

    asunto = forms.CharField(
        label='Asunto',
        max_length=100,
        error_messages={
           'required':'Por favor, ingrese el asunto'
        },
        validators=(solo_caracteres,),
        widget=forms.TextInput(attrs={'class':'form-control'})
        )

    '''asunto = forms.IntegerField(max_length=50,choices=opciones_asunto,default=1)'''

    mensaje = forms.CharField(
        label='Mensaje',
        max_length=500,
        error_messages={
            'required':'Por favor, escriba el mensaje'
        },
        widget=forms.Textarea(attrs={'class':'form-control','rows':5,})
        )

    novedad = forms.BooleanField(
        label='Deseo recibir novedades!',
        required=False,
        widget=forms.CheckboxInput(attrs={'class':'form-check-input','value':1})
    )

    def clean_mensaje(self):
        data = self.cleaned_data['mensaje']
        if len(data) < 10:
            raise ValidationError('Debe especificar mejor el mensaje')
        return data

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(
        widget=forms.TextInput(attrs={'class':'form-control','type':'email','placeholder':'info@gmail.com'})
    )
    password1 = forms.CharField(label='Contraseña',widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar Contraseña',widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k:"" for k in fields} #para que no aparezcan los textos de ayuda
