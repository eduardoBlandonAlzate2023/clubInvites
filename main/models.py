# main/models.py

from django.db import models
from django.contrib.auth.models import User

class UserFormData(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Changed from ForeignKey to OneToOneField
    perfil_descripcion = models.TextField("Descripción de perfil (estilo LinkedIn)")
    empresas_y_logros = models.TextField("Empresas en las que ha trabajado y sus logros")
    anos_experiencia_liderazgo = models.PositiveIntegerField(
        "¿Cuántos años de experiencia tiene en posiciones de liderazgo o dirección?"
    )
    numero_juntas_anteriores = models.PositiveIntegerField(
        "¿Cuántas juntas directivas ha integrado anteriormente?"
    )
    ha_ocupado_posicion_ejecutiva = models.BooleanField(
        "¿Ha ocupado posiciones ejecutivas?", default=False
    )
    anos_en_posicion_ejecutiva = models.PositiveIntegerField(
        "Si respondió 'Sí', ¿cuánto tiempo ocupó esa posición? (Años)", null=True, blank=True
    )
    horas_mensuales_disponibles = models.PositiveIntegerField(
        "¿Cuántas horas mensuales puede dedicar al trabajo de la junta?"
    )
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.perfil_descripcion[:30]}..."

class Competencia(models.Model):
    user_form_data = models.ForeignKey(UserFormData, on_delete=models.CASCADE, related_name='competencias')
    nombre = models.CharField("Competencia", max_length=100)

    def __str__(self):
        return self.nombre