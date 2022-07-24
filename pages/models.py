from django.db import models
from ckeditor.fields import RichTextField
 
# Create your models here.
class Seccion(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de Modificación")

    class Meta:
        verbose_name = "seccion"
        verbose_name_plural = "secciones"
        ordering = ['-created']

    def __str__(self):
        return self.name

class Page(models.Model):
    title = models.CharField(verbose_name="Título", max_length=200)
    content = RichTextField(verbose_name="Contenido")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de Modificación")
    imagePage = models.ImageField(verbose_name="Imagen", upload_to="pages", null=True, blank=True)
    seccionPage = models.ForeignKey(Seccion, verbose_name="Sección", related_name="get_seccion", on_delete=models.CASCADE)
 
    class Meta:
        verbose_name = "página"
        verbose_name_plural = "páginas"
        ordering = ['title']
 
    def __str__(self):
        return self.title
