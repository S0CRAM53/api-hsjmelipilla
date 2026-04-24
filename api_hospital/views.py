from rest_framework import viewsets
from .models import Servicio, Indicador, ValorIndicador
from .serializers import ServicioSerializer, IndicadorSerializer, ValorIndicadorSerializer

class ServicioViewSet(viewsets.ModelViewSet):
    queryset = Servicio.objects.all()
    serializer_class = ServicioSerializer

class IndicadorViewSet(viewsets.ModelViewSet):
    queryset = Indicador.objects.all()
    serializer_class = IndicadorSerializer

class ValorIndicadorViewSet(viewsets.ModelViewSet):
    queryset = ValorIndicador.objects.all()
    serializer_class = ValorIndicadorSerializer

    # Permitir filtrar por servicio y año en la URL
    def get_queryset(self):
        queryset = ValorIndicador.objects.all()
        servicio = self.request.query_params.get('servicio')
        anio = self.request.query_params.get('anio')
        
        if servicio:
            queryset = queryset.filter(servicio_id=servicio)
        if anio:
            queryset = queryset.filter(anio=anio)
        return queryset