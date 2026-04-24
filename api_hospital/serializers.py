from rest_framework import serializers
from .models import Servicio, Indicador, ValorIndicador

class ServicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servicio
        fields = '__all__'

class IndicadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Indicador
        fields = '__all__'

class ValorIndicadorSerializer(serializers.ModelSerializer):
    # Incluimos el nombre del servicio e indicador en lugar de solo el ID
    servicio_nombre = serializers.ReadOnlyField(source='servicio.nombre')
    indicador_nombre = serializers.ReadOnlyField(source='indicador.nombre')

    class Meta:
        model = ValorIndicador
        fields = [
            'id', 'servicio', 'servicio_nombre', 'indicador', 
            'indicador_nombre', 'anio', 'mes', 'valor_calculado'
        ]