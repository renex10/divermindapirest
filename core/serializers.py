# core/serializers.py
from rest_framework import serializers
from .models import (
    Nino, ObservacionEscuela, ObservacionFamilia, Autismo, Diagnostico,
    DetonanteCrisis, Debilidad, PerfilPersonal, HitoDesarrollo, ControlEsfinteres,
    Alimentacion, Sueno, SensibilidadSensorial, ActividadExtracurricular, Autorizacion
)

class PerfilPersonalSerializer(serializers.ModelSerializer):
    class Meta:
        model = PerfilPersonal
        fields = '__all__'

class NinoSerializer(serializers.ModelSerializer):
    perfil = PerfilPersonalSerializer(source='id_perfil')
    direccion = serializers.StringRelatedField()

    class Meta:
        model = Nino
        fields = ['id', 'perfil', 'necesidades_especiales', 'direccion', 'familias']
        depth = 1

class ObservacionEscuelaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ObservacionEscuela
        fields = '__all__'

class ObservacionFamiliaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ObservacionFamilia
        fields = '__all__'

class AutismoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autismo
        fields = '__all__'

class DiagnosticoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diagnostico
        fields = '__all__'

class DetonanteCrisisSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetonanteCrisis
        fields = '__all__'

class DebilidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Debilidad
        fields = '__all__'

# Nuevos serializers
class HitoDesarrolloSerializer(serializers.ModelSerializer):
    class Meta:
        model = HitoDesarrollo
        fields = '__all__'

class ControlEsfinteresSerializer(serializers.ModelSerializer):
    class Meta:
        model = ControlEsfinteres
        fields = '__all__'

class AlimentacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alimentacion
        fields = '__all__'

class SuenoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sueno
        fields = '__all__'

class SensibilidadSensorialSerializer(serializers.ModelSerializer):
    class Meta:
        model = SensibilidadSensorial
        fields = '__all__'

class ActividadExtracurricularSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActividadExtracurricular
        fields = '__all__'

class AutorizacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autorizacion
        fields = '__all__'