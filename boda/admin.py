from django.contrib import admin
from boda.models import *


@admin.register(WebPassword)
class WebPasswordAdmin(admin.ModelAdmin):
    list_display = ['password', 'is_required']


@admin.register(Confirmacion)
class ConfirmacionAdmin(admin.ModelAdmin):
    list_display = ['asistiras', 'surname', 'name',
                    'bus_ida', 'bus_vuelta', 'acompanantes', 'food_restrictions', 'nombre_cancion', 'nombre_grupo']
    list_filter = ['asistiras', 'bus_ida', 'bus_vuelta',
                   'food_restrictions', 'acompanantes']
    search_fields = ['name', 'surname',
                     'food_restrictions_especificaciones', 'nombre_cancion', 'nombre_grupo', 'nombres_acompanantes']
    fieldsets = (
        ('Datos personales', {
            'fields': ('asistiras', 'name', 'surname')
        }),
        ('Acompañantes', {
            'fields': ('acompanantes', 'nombres_acompanantes')
        }),
        ('Datos de interés', {
            'fields': ('bus_ida', 'bus_vuelta', 'food_restrictions', 'food_restrictions_especificaciones', 'nombre_cancion', 'nombre_grupo')
        })
    )


@admin.register(Itinerario)
class ItinerarioAdmin(admin.ModelAdmin):
    list_display = ['name', 'start_time', 'end_time']
    list_filter = ['start_time', 'end_time', 'name']
    fieldsets = (
        ('Información evento', {
            'fields': ('name', 'description', 'start_time', 'end_time')
        }),
        ('Localización', {
            'fields': ('location_name', 'location_url', 'image')
        })
    )


@admin.register(Cancion)
class CancionAdmin(admin.ModelAdmin):
    list_display = ['nombre']


# MODIFICABLES WEB

@admin.register(LugarDeLaBoda)
class LugarDeLaBodaAdmin(admin.ModelAdmin):
    list_display = ['name', 'mensaje']


@admin.register(ItinerarioHeader)
class ItinerarioHeaderAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']


@admin.register(NombresPareja)
class NombresParejaAdmin(admin.ModelAdmin):
    list_display = ['novia', 'novio']

    fieldsets = (
        ('Novia', {
            'fields': ('novia', 'descripcion_novia')
        }),
        ('Novio', {
            'fields': ('novio', 'descripcion_novio')
        })
    )


@admin.register(FechaDeBoda)
class FechaDeBodaAdmin(admin.ModelAdmin):
    list_display = ['fecha']


@admin.register(Autobus)
class AutobusAdmin(admin.ModelAdmin):
    list_display = ['origen', 'destino']
