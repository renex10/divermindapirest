from django.db import models

class Pais(models.Model):
    nombre = models.CharField(max_length=100)
    codigo_iso = models.CharField(max_length=2, unique=True)

    def __str__(self):
        return self.nombre


class Region(models.Model):
    nombre = models.CharField(max_length=100)
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre


class Comuna(models.Model):
    nombre = models.CharField(max_length=100)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

