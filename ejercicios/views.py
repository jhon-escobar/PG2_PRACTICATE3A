from django.shortcuts import render

# Python native imports
from datetime import timedelta

# External imports
from rest_framework import viewsets
from django.utils import timezone as tz

# Local imports
from ejercicios.serializers import *
from ejercicios.models import *


class disiplinaViewSet(viewsets.ModelViewSet):
    queryset = disiplina.objects.all()
    serializer_class = disiplinaSerializer


class CertificacionViewSet(viewsets.ModelViewSet):
    queryset = Certificacion.objects.all()
    serializer_class = CertificacionSerializer


class CertificacionViewSet(viewsets.ModelViewSet):
    queryset = Certificacion.objects.all()
    serializer_class = CertificacionSerializer


class RecomendacionViewSet(viewsets.ModelViewSet):
    queryset = Recomendacion.objects.all()
    serializer_class = RecomendacionSerializer


class tipoCompetenciaViewSet(viewsets.ModelViewSet):
    queryset = tipoCompetencia.objects.all()
    serializer_class = tipoCompetenciaSerializer


class reglaViewSet(viewsets.ModelViewSet):
    queryset = regla.objects.all()
    serializer_class = reglaSerializer


class expertoViewSet(viewsets.ModelViewSet):
    queryset = experto.objects.all()
    serializer_class = expertoSerializer
