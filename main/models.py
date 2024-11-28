# main/models.py

from django.db import models
from django.contrib.auth.models import User

class UserFormData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    # 1. Descripción de perfil (estilo LinkedIn)
    perfil_descripcion = models.TextField("Descripción de perfil (estilo LinkedIn)")
    
    # 2. Empresas en las que ha trabajado y logros
    empresas_y_logros = models.TextField("Empresas en las que ha trabajado y sus logros")
    
    # 3. Años de experiencia en posiciones de liderazgo o dirección
    anos_experiencia_liderazgo = models.PositiveIntegerField(
        "¿Cuántos años de experiencia tiene en posiciones de liderazgo o dirección?"
    )
    
    # 4. Número de juntas directivas integradas anteriormente
    numero_juntas_anteriores = models.PositiveIntegerField(
        "¿Cuántas juntas directivas ha integrado anteriormente?"
    )
    
    # 5. Ha ocupado posiciones ejecutivas (CEO, CFO, COO, etc.)
    ha_ocupado_posicion_ejecutiva = models.BooleanField(
        "¿Ha ocupado posiciones ejecutivas (CEO, CFO, COO, etc.)?", default=False
    )
    
    # Si respondió "Sí", ¿cuánto tiempo ocupó esa posición? (Años)
    anos_en_posicion_ejecutiva = models.PositiveIntegerField(
        "Si respondió 'Sí', ¿cuánto tiempo ocupó esa posición? (Años)", null=True, blank=True
    )
    
    # 6. ¿Cuántas horas mensuales puede dedicar al trabajo de la junta?
    horas_mensuales_disponibles = models.PositiveIntegerField(
        "¿Cuántas horas mensuales puede dedicar al trabajo de la junta?"
    )
    
    # 7. Competencias de mayor conocimiento o experticia
    competencias = models.CharField(
        "Competencias de mayor conocimiento o experticia (tecnología, marketing, ventas, etc.)",
        max_length=255
    )
    
    # Fecha de envío
    submitted_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user.username} - {self.perfil_descripcion[:30]}..."
