from ejercicios.models import *
from rest_framework import serializers


class displinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = disiplina
        fields = [
            "id",
            "nombre",
            "nombre_certificacion",
            "foto",
            "titulo",
            "descripcion",
            "detalle",
            "estilo",
            "distancia",
            "tiempo",
            "numero",
            "norma_establecida",
            "area",
        ]


class disiplinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = disiplina
