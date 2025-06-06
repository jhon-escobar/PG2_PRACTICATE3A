"""
URL configuration for apichapapintura project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# Django imports
from django.contrib import admin
from django.urls import path, include

# Rest framework imports
from rest_framework import routers

# Local imports
from ejercicios.views import (
    disiplinaViewSet,
    CertificacionViewSet,
    RecomendacionViewSet,
    tipoCompetenciaViewSet,
    reglaViewSet,
    expertoViewSet,
)

# Create a router and register our viewset with it.
router = routers.DefaultRouter()

router.register(r"disiplina", disiplinaViewSet)
router.register(r"Certificacion", CertificacionViewSet)
router.register(r"Recomendacion", RecomendacionViewSet)
router.register(r"tipo Competencia", tipoCompetenciaViewSet)
router.register(r"regla", reglaViewSet)
router.register(r"experto", expertoViewSet)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
]
