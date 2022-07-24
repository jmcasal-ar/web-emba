from django.contrib import admin
from .models import Page, Seccion
# Register your models here.
 
class PageAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class SeccionAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    
admin.site.register(Page, PageAdmin)
admin.site.register(Seccion, SeccionAdmin)
