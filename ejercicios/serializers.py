from ejercicios.models import *
from rest_framework import serializers


class disiplinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = disiplina
        fields = [
            "nombre",
            "foto",
        ]


class CertificacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificacion
        fields = [
            "nombre certificacion",
            "fecha de emision",
        ]


class RecomendacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recomendacion
        fields = [
            "titulo",
            "descripcion",
        ]


class tipoCompetenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = tipoCompetencia
        fields = [
            "nobre",
            "detalle",
            "estilo",
            "distancia",
            "yiempo",
        ]


class reglaSerializer(serializers.ModelSerializer):
    class Meta:
        model = regla
        fields = [
            "numero",
            "detalle",
            "norma_establecida",
        ]


class expertoSerializer(serializers.ModelSerializer):
    class Meta:
        model = experto
        fields = [
            "nombre",
            "area",
        ]
