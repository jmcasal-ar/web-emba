from django.contrib import admin
from .models import Carrera, Area

# Register your models here.

class AreaAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


class CarreraAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    #Visualizamos columnas en el panel. El __ se usa para campos relacionales
    list_display = ('name', 'published')
    #ordenamos el panel
    ordering = ('published', 'name' ) 
    #agregamos una caja de busqueda por los siguientes campos
    search_fields = ('published', 'area' ) 
    #agregamos un panel de visualización por jerarquia
    date_hierarchy = 'published'



admin.site.register(Area, AreaAdmin)
admin.site.register(Carrera, CarreraAdmin)