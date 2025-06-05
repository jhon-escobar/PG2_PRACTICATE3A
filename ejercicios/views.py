from django.shortcuts import render

# Create your views here.
from datetime import timedelta

# External imports
from rest_framework import viewsets
from django.utils import timezone as tz

# Local imports
from ejercicios.serializers import *
from ejercicios.models import *


class ejerciciosViewSet(viewsets.ModelViewSet):
    queryset = ejercicios.objects.filter(
        fecha_hora_matricula__lte=tz.localtime() - timedelta(minutes=1)
    )
    serializer_class = ejerciciosSerializer


class MateriaViewSet(viewsets.ModelViewSet):
    queryset = disiplina.objects.all()
    serializer_class = disiplinaSerializer
