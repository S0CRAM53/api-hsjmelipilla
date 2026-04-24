from django.db import models

class Servicio(models.Model):
    nombre = models.CharField(max_length=100, unique=True, verbose_name="Nombre del Servicio")

    def __str__(self):
        return self.nombre

class Indicador(models.Model):
    nombre = models.CharField(max_length=150, unique=True)
    formula = models.TextField(help_text="Descripción textual de la fórmula")
    unidad = models.CharField(max_length=50, help_text="Ej: entero o porcentaje")

    def __str__(self):
        return self.nombre

class ValorIndicador(models.Model):
    MESES = [
        (1, 'Enero'), (2, 'Febrero'), (3, 'Marzo'), (4, 'Abril'),
        (5, 'Mayo'), (6, 'Junio'), (7, 'Julio'), (8, 'Agosto'),
        (9, 'Septiembre'), (10, 'Octubre'), (11, 'Noviembre'), (12, 'Diciembre'),
    ]

    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE, related_name='valores')
    indicador = models.ForeignKey(Indicador, on_delete=models.CASCADE, related_name='valores')
    anio = models.IntegerField(default=2025)
    mes = models.IntegerField(choices=MESES)
    valor_calculado = models.FloatField()

    class Meta:
        unique_together = ('servicio', 'indicador', 'anio', 'mes')
        verbose_name = "Valor de Indicador"
        verbose_name_plural = "Valores de Indicadores"

    def __str__(self):
        return f"{self.indicador.nombre} - {self.servicio.nombre} ({self.mes}/{self.anio})"