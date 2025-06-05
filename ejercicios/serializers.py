from ejercicios.models import *
from rest_framework import serializers


class ejerciciosteSerializer(serializers.ModelSerializer):
    class Meta:
        model = disiplina
        fields = [
            "nombre",
            "foto",
        ]


class disiplinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificacion
        fields = [
            "nombre certificacion",
            "fecha de emision",
        ]


class disiplinaserializer(serializers.ModelSerializer):
    class Meta:
        model = tipoCompetencia
        fields = [
            "nobre",
            "detalle",
            "estilo",
            "distancia",
            "yiempo",
        ]


class disiplinaserializer(serializers.ModelSerializer):
    class Meta:
        model = regla
        fields = [
            "numero",
            "detalle",
            "norma_establecida",
        ]


class disiplinaserializer(serializers.ModelSerializer):
    class Meta:
        model = experto
        fields = [
            "nombre",
            "area",
        ]
