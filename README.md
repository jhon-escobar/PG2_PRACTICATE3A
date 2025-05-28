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
