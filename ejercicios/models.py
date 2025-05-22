from django.db import models


class disiplina(models.Model):
    nombre = models.CharField(max_length=150)
    foto = models.CharField(max_length=150)

    def __str__(self):
        return self.nombre


class tipoCompetencia(models.Model):
    nombre = models.CharField(max_length=150)
    detalle = models.CharField(max_length=150)
    estilo = models.CharField(max_length=150)
    distancia = models.CharField(max_length=150)
    tiempo = models.CharField(max_length=150)

    disiplina = models.ForeignKey(
        disiplina, on_delete=models.CASCADE, related_name="tipos_competencia"
    )
    disiplina = models.ForeignKey(
        disiplina, on_delete=models.CASCADE, related_name="tipos_competencia"
    )

    reglas = models.ManyToManyField("regla", related_name="tipos_competencia")

    recomendaciones = models.ManyToManyField(
        "Recomendacion", related_name="tipos_competencia"
    )

    # Opcional: Añadir un método __str__ para una representación legible del objeto
    def __str__(self):
        return f"{self.nombre} ({self.disiplina.nombre})"


class recomendacion(models.Model):
    id = models.CharField(max_length=150)
    descripcion = models.TextField()

    def __str__(self):
        return self.titulo


class regla(models.Model):
    numero = models.CharField(max_length=150)
    detalle = models.CharField(max_length=150)
    norma_establecida = models.CharField(max_length=150)

    def __str__(self):
        return f"Regla {self.numero}"


class experto(models.Model):
    nombre = models.CharField(max_length=150)
    area = models.CharField(max_length=150)

    def __str__(self):
        return self.nombre
