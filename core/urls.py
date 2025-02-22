# core/urls.py
from django.urls import path
from .views import (
    NinoListCreateAPIView, ObservacionEscuelaCreateAPIView, ObservacionFamiliaCreateAPIView,
    AutismoRetrieveUpdateAPIView, DiagnosticoListCreateAPIView, DetonanteCrisisListCreateAPIView,
    DebilidadListCreateAPIView, NinoDestroyAPIView, NinoRetrieveUpdateAPIView,
    HitoDesarrolloListCreateAPIView, ControlEsfinteresRetrieveUpdateAPIView,
    AlimentacionRetrieveUpdateAPIView, SuenoRetrieveUpdateAPIView,
    SensibilidadSensorialListCreateAPIView, ActividadExtracurricularListCreateAPIView,
    AutorizacionRetrieveUpdateAPIView
)

urlpatterns = [
    path('ninos/', NinoListCreateAPIView.as_view(), name='nino-list'),
    path('ninos/<int:pk>/', NinoRetrieveUpdateAPIView.as_view(), name='nino-detail'),
    path('ninos/<int:pk>/delete/', NinoDestroyAPIView.as_view(), name='nino-delete'),
    
    # Secciones del formulario
    path('ninos/<int:nino_id>/diagnosticos/', DiagnosticoListCreateAPIView.as_view(), name='diagnostico-list'),
    path('ninos/<int:nino_id>/detonantes-crisis/', DetonanteCrisisListCreateAPIView.as_view(), name='detonante-crisis-list'),
    path('ninos/<int:nino_id>/debilidades/', DebilidadListCreateAPIView.as_view(), name='debilidad-list'),
    path('ninos/<int:nino_id>/hitos-desarrollo/', HitoDesarrolloListCreateAPIView.as_view(), name='hitos-desarrollo'),
    path('ninos/<int:nino_id>/control-esfinteres/', ControlEsfinteresRetrieveUpdateAPIView.as_view(), name='control-esfinteres'),
    path('ninos/<int:nino_id>/alimentacion/', AlimentacionRetrieveUpdateAPIView.as_view(), name='alimentacion'),
    path('ninos/<int:nino_id>/sueno/', SuenoRetrieveUpdateAPIView.as_view(), name='sueno'),
    path('ninos/<int:nino_id>/sensibilidades/', SensibilidadSensorialListCreateAPIView.as_view(), name='sensibilidades'),
    path('ninos/<int:nino_id>/actividades/', ActividadExtracurricularListCreateAPIView.as_view(), name='actividades'),
    path('ninos/<int:nino_id>/autorizaciones/', AutorizacionRetrieveUpdateAPIView.as_view(), name='autorizaciones'),
    
    # Otras rutas
    path('observaciones-escuela/', ObservacionEscuelaCreateAPIView.as_view(), name='observacion-escuela-create'),
    path('observaciones-familia/', ObservacionFamiliaCreateAPIView.as_view(), name='observacion-familia-create'),
    path('autismo/<int:pk>/', AutismoRetrieveUpdateAPIView.as_view(), name='autismo-detail'),
]