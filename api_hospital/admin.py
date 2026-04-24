from django.contrib import admin
from .models import Servicio, Indicador, ValorIndicador

@admin.register(Servicio)
class ServicioAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')

@admin.register(Indicador)
class IndicadorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'unidad')

@admin.register(ValorIndicador)
class ValorIndicadorAdmin(admin.ModelAdmin):
    list_display = ('indicador', 'servicio', 'mes', 'anio', 'valor_calculado')
    list_filter = ('servicio', 'anio', 'mes')