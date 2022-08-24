from django.contrib import admin

# Register your models here.
from .models import Artesania, Opinion

class AdministrarArtesania(admin.ModelAdmin):
    readonly_fields=('created','updated')
    list_display=('id','nombre','descripcion','municipio','created')
    search_fields=('id','nombre','descripcion','costo')
    date_hierarchy='created'
    list_filter=('municipio','costo')
    list_per_page=2
    list_display_links=('municipio','nombre')

admin.site.register(Artesania, AdministrarArtesania)

class AdministrarOpiniones(admin.ModelAdmin):
    list_display=('id','comentario')
    search_fields=('id','created')
    date_hierarchy='created'
    readonly_fields=('created','id')

admin.site.register(Opinion,AdministrarOpiniones)