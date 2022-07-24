from django.db import models
from django.utils import timezone #Imporza libreria de fechas
from django.contrib.auth.models import User #importar usuarios creados con el panel de admin
from ckeditor.fields import RichTextField

# Create your models here.
class Area(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de Modificación")

    class Meta:
        verbose_name = "area"
        verbose_name_plural = "areas"
        ordering = ['-created']

    def __str__(self):
        return self.name

class Carrera(models.Model):
    name = models.CharField(max_length=200, verbose_name="Título")
    subtitle = models.CharField(max_length=200, verbose_name="Subtítulo")
    content = RichTextField(verbose_name="Contenido")
    published = models.DateTimeField(verbose_name="Fecha de Publicación", default=timezone.now)
    imageCarrera = models.ImageField(verbose_name="Imagen", upload_to="carreras", null=True, blank=True)
    color = models.CharField(max_length=10, verbose_name="Color")
    #Enlazar con Foreign Key en cascada
    areaCarrera = models.ForeignKey(Area, verbose_name="Área", related_name="get_areas", on_delete=models.CASCADE)
    created = models.DateTimeField(verbose_name="Fecha de Creación", auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de Modificación")

    class Meta:
        verbose_name = "carrera"
        verbose_name_plural = "carreras"
        ordering = ['-created']

    def __str__(self):
        return self.name