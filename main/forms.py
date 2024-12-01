# main/forms.py

from django import forms
from .models import Competencia, UserFormData
from django.forms import Textarea, TextInput, NumberInput, CheckboxInput, PasswordInput, inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
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
            'competencias': 'Competencias de mayor conocimiento o experticia (tecnología, marketing, ventas, etc.)',
        }
        help_texts = {
            'perfil_descripcion': 'Ingrese una descripción de su perfil similar a la de LinkedIn.',
            'empresas_y_logros': 'Mencione las empresas y describa brevemente sus logros en cada una.',
            'anos_en_posicion_ejecutiva': 'Complete este campo solo si ha ocupado posiciones ejecutivas.',
        }
        widgets = {
            'perfil_descripcion': Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'empresas_y_logros': Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'anos_experiencia_liderazgo': NumberInput(attrs={'class': 'form-control'}),
            'numero_juntas_anteriores': NumberInput(attrs={'class': 'form-control'}),
            'ha_ocupado_posicion_ejecutiva': CheckboxInput(attrs={'class': 'form-check-input'}),
            'anos_en_posicion_ejecutiva': NumberInput(attrs={'class': 'form-control'}),
            'horas_mensuales_disponibles': NumberInput(attrs={'class': 'form-control'}),
            'competencias': TextInput(attrs={'class': 'form-control'}),
    }
    
    def clean(self):
        cleaned_data = super().clean()
        ha_ocupado = cleaned_data.get('ha_ocupado_posicion_ejecutiva')
        anos_ejecutiva = cleaned_data.get('anos_en_posicion_ejecutiva')
        
        if ha_ocupado and not anos_ejecutiva:
            self.add_error('anos_en_posicion_ejecutiva', 'Por favor, indique cuántos años ocupó esa posición.')
        elif not ha_ocupado:
            cleaned_data['anos_en_posicion_ejecutiva'] = None
        return cleaned_data

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')
        labels = {
            'username': 'Nombre de usuario',
            'password1': 'Contraseña',
            'password2': 'Confirmar contraseña',
        }
        help_texts = {
            'username': None,
            'password1': None,
            'password2': None,
        }
        widgets = {
            'username': TextInput(attrs={'class': 'form-control'}),
            'password1': PasswordInput(attrs={'class': 'form-control'}),
            'password2': PasswordInput(attrs={'class': 'form-control'}),
        }

class CompetenciaForm(forms.ModelForm):
    class Meta:
        model = Competencia
        fields = ['nombre']
        labels = {
            'nombre': 'Competencia',
        }
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