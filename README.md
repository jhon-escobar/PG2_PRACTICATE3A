# PG2_PRACTICATE3A

# My API

la paractica consiste en hacer una API enfocado en la disiplina llamada atletismo que dara la infotmacion de :

<p>Disiplina
<p>Tipo Conpetencia
<p>Regla
<p>recomendacion
<p>Experto
<p>Certificacion

# API

el api tendra estos atributos segun la entidad.

### Disiplina

```python

class disiplina(models.Model):
    nombre = models.CharField(max_length=150)
    foto = models.CharField(max_length=150)

```

### Tipo Competencia

```python
class tipoCompetencia(models.Model):
    nombre = models.CharField(max_length=150)
    detalle = models.CharField(max_length=150)
    estilo = models.CharField(max_length=150)
    distancia = models.CharField(max_length=150)
    tiempo = models.CharField(max_length=150)


```

### Regla

```python
class regla(models.Model):
    numero = models.CharField(max_length=150)
    detalle = models.CharField(max_length=150)
    norma_establecida = models.CharField(max_length=150)

```

### Recomendacion

```python

class Recomendacion(models.Model):
    titulo = models.CharField(max_length=150)
    descripcion = models.TextField()


```

### Expeto

```python
class experto(models.Model):
    nombre = models.CharField(max_length=150)
    area = models.CharField(max_length=150)


```

### Certificacion

```python

class Certificacion(models.Model):
    nombre_certificacion = models.CharField(max_length=150)
    fecha_emision = models.DateField()


```

#### de esta manera veriamos el codigo completo incliyendo la entidad relacion definiendo las llaves primarias, foranias

```python
from django.db import models

class disiplina(models.Model):
nombre = models.CharField(max_length=150)
foto = models.CharField(max_length=150)

    def __str__(self):
        return self.nombre

class Certificacion(models.Model):
nombre_certificacion = models.CharField(max_length=150)
fecha_emision = models.DateField()

    experto = models.OneToOneField(
        "experto", on_delete=models.CASCADE, related_name="certificacion"
    )

    def __str__(self):
        return f"Certificación: {self.nombre_certificacion} ({self.experto.nombre})"

class Recomendacion(models.Model):
titulo = models.CharField(max_length=150)
descripcion = models.TextField()

    def __str__(self):
        return self.titulo

class tipoCompetencia(models.Model):
nombre = models.CharField(max_length=150)
detalle = models.CharField(max_length=150)
estilo = models.CharField(max_length=150)
distancia = models.CharField(max_length=150)
tiempo = models.CharField(max_length=150)

    disiplina = models.ForeignKey(
        disiplina, on_delete=models.CASCADE, related_name="tipos_competencia"
    )

    reglas = models.ManyToManyField("regla", related_name="tipos_competencia")

    recomendaciones = models.ManyToManyField(
        "Recomendacion", related_name="tipos_competencia_asociadas"
    )

    def __str__(self):
        return f"{self.nombre} ({self.disiplina.nombre})"

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

```

### Imagen del Diagrama.png

![Texto alternativo de la imagen](https://github.com/jhon-escobar/PG2_PRACTICATE3A/blob/08d2013c0d040834f9e9b599c501fa9da5510f44/png/Annotation%202025-05-27%20220525.png)
