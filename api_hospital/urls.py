from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ServicioViewSet, IndicadorViewSet, ValorIndicadorViewSet

router = DefaultRouter()
router.register(r'servicios', ServicioViewSet)
router.register(r'indicadores', IndicadorViewSet)
router.register(r'valores', ValorIndicadorViewSet)

urlpatterns = [
    path('', include(router.urls)),
]