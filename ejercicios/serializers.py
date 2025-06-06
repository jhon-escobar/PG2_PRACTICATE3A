from ejercicios.models import *
from rest_framework import serializers


class disiplinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = disiplina
        fields = "_all_"


class CertificacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificacion
        fields = "_all_"


class RecomendacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recomendacion
        fields = "_all_"


class tipoCompetenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = tipoCompetencia
        fields = "_all_"


class reglaSerializer(serializers.ModelSerializer):
    class Meta:
        model = regla
        fields = "_all_"


class expertoSerializer(serializers.ModelSerializer):
    class Meta:
        model = experto
        fields = "_all_"
