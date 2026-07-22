from django import forms 
from django.forms import ModelForm
from django.forms import widgets
from django.forms.widgets import Widget
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Helados, Barquillo


class HeladoForm(forms.ModelForm):
    class Meta:
        model = Helados
        fields = ['id', 'rango', 'cantidad','sabor', 'barquillo','precio', 'imagen']
        labels ={
            'id': 'Id Helado',
            'rango': 'Rango',
            'cantidad': 'Cantidad',
            'sabor': 'Sabor',
            'barquillo': 'Barquillo',
            'precio': 'Precio',
            'imagen': 'Imagen'
        }
        widgets={
            'id': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Ingrese Id Helado',
                    'id': 'id'
                }
            ),
            'rango': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Ingrese rango Helado',
                    'id': 'rango'
                }
            ),
            'cantidad': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Ingrese cantidad de Helados',
                    'id': 'cantidad'
                }
            ),
            'sabor': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Ingrese sabor de Helados',
                    'id': 'sabor'
                }
            ),
            'barquillo': forms.Select( 
                attrs={
                    'class': 'form-control',
                    'id': 'barquillo'
                }
            ),

            'precio': forms.NumberInput( 
                attrs={
                    'class': 'form-control',
                    'id': 'precio'
                }
            ),
            'imagen': forms.FileInput(
                attrs={
                    'class': 'form-control',
                    'id': 'imagen'
                }
            )

        }

class PerfilModificacion(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
        labels = {
            'first_name': 'Nombre: ',
            'last_name': 'Apellido: ',
            'email': 'Correo: '
        }
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su nombre',
                    'id': 'first_name'
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su apellido',
                    'id': 'last_name'
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su correo',
                    'id': 'email'
                }
            )
        }
class RegistroUserForm(UserCreationForm):
    password1 = forms.CharField(
        label="Contraseña",
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese su contraseña',
                'id': 'password1'
            }
        )
    )
    password2 = forms.CharField(
        label="Confirmar contraseña",
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Confirme su contraseña',
                'id': 'password2'
            }
        )
    )

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
        labels = {
            'username': 'Nombre de usuario',
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'email': 'Correo',
            'password1': 'Contraseña',
            'password2': 'Confirmar contraseña'
        }
        widgets = {
            'username': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su nombre de usuario',
                    'id': 'username'
                }
            ),
            'first_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su nombre',
                    'id': 'first_name'
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su apellido',
                    'id': 'last_name'
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su correo',
                    'id': 'email'
                }
            )
        }