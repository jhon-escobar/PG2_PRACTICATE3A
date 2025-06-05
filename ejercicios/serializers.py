from ejercicios.models import *
from rest_framework import serializers


class ejerciciosteSerializer(serializers.ModelSerializer):
    class Meta:
        model = disiplina
        fields = [
            "id",
            "nombre",
            "apellido",
            "fecha_hora_matricula",
            "apodo",
            "intereses",
            "ciudad",
            "pais",
            "edad",
            "correo",
        ]


class disiplinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = disiplina
        fields = "__all__"
