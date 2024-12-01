from django import forms
from .models import Competencia, UserFormData
from django.forms import Textarea, TextInput, NumberInput, CheckboxInput, PasswordInput, inlineformset_factory
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    class Meta:
        model = UserFormData
        fields = [
            'perfil_descripcion',
            'empresas_y_logros',
            'anos_experiencia_liderazgo',
            'numero_juntas_anteriores',
            'ha_ocupado_posicion_ejecutiva',
            'anos_en_posicion_ejecutiva',
            'horas_mensuales_disponibles',
        ]
        labels = {
            'perfil_descripcion': 'Descripción de perfil',
            'empresas_y_logros': 'Empresas en las que ha trabajado y sus logros',
            'anos_experiencia_liderazgo': '¿Cuántos años de experiencia tiene en posiciones de liderazgo o dirección?',
            'numero_juntas_anteriores': '¿Cuántas juntas directivas ha integrado anteriormente?',
            'ha_ocupado_posicion_ejecutiva': '¿Ha ocupado posiciones ejecutivas?',
            'anos_en_posicion_ejecutiva': "Si respondió 'Sí', ¿cuánto tiempo ocupó esa posición? (Años)",
            'horas_mensuales_disponibles': '¿Cuántas horas mensuales puede dedicar al trabajo de la junta?',
        }
        widgets = {
            'perfil_descripcion': Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'empresas_y_logros': Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'anos_experiencia_liderazgo': NumberInput(attrs={'class': 'form-control'}),
            'numero_juntas_anteriores': NumberInput(attrs={'class': 'form-control'}),
            'ha_ocupado_posicion_ejecutiva': CheckboxInput(attrs={'class': 'form-check-input'}),
            'anos_en_posicion_ejecutiva': NumberInput(attrs={'class': 'form-control'}),
            'horas_mensuales_disponibles': NumberInput(attrs={'class': 'form-control'}),
        }


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')
        labels = {
            'username': 'Nombre de usuario',
            'password1': 'Contraseña',
            'password2': 'Confirmar contraseña',
        }
        widgets = {
            'username': TextInput(attrs={'class': 'form-control'}),
            'password1': PasswordInput(attrs={'class': 'form-control'}),
            'password2': PasswordInput(attrs={'class': 'form-control'}),
        }


class CustomAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(
        label="Correo",
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su correo'}),
    )
    password = forms.CharField(
        label="Contraseña",
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su contraseña'}),
    )


class CompetenciaForm(forms.ModelForm):
    class Meta:
        model = Competencia
        fields = ['nombre']
        widgets = {
            'nombre': TextInput(attrs={'class': 'form-control'}),
        }


CompetenciaFormSet = inlineformset_factory(
    UserFormData,
    Competencia,
    form=CompetenciaForm,
    extra=1,
    can_delete=True
)
