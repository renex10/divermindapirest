# core/views.py
from rest_framework import generics, permissions
from .models import (
    Nino, ObservacionEscuela, ObservacionFamilia, Autismo, Diagnostico,
    DetonanteCrisis, Debilidad, HitoDesarrollo, ControlEsfinteres,
    Alimentacion, Sueno, SensibilidadSensorial, ActividadExtracurricular, Autorizacion
)
from .serializers import (
    NinoSerializer, ObservacionEscuelaSerializer, ObservacionFamiliaSerializer,
    AutismoSerializer, DiagnosticoSerializer, DetonanteCrisisSerializer,
    DebilidadSerializer, HitoDesarrolloSerializer, ControlEsfinteresSerializer,
    AlimentacionSerializer, SuenoSerializer, SensibilidadSensorialSerializer,
    ActividadExtracurricularSerializer, AutorizacionSerializer
)

class NinoListCreateAPIView(generics.ListCreateAPIView):
    queryset = Nino.objects.all()
    serializer_class = NinoSerializer
    permission_classes = [permissions.AllowAny]

class NinoRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Nino.objects.all()
    serializer_class = NinoSerializer
    permission_classes = [permissions.IsAuthenticated]

class NinoDestroyAPIView(generics.DestroyAPIView):
    queryset = Nino.objects.all()
    serializer_class = NinoSerializer
    permission_classes = [permissions.IsAuthenticated]

# Vistas existentes
class ObservacionEscuelaCreateAPIView(generics.CreateAPIView):
    queryset = ObservacionEscuela.objects.all()
    serializer_class = ObservacionEscuelaSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(profesor=self.request.user)

class ObservacionFamiliaCreateAPIView(generics.CreateAPIView):
    queryset = ObservacionFamilia.objects.all()
    serializer_class = ObservacionFamiliaSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)

class AutismoRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Autismo.objects.all()
    serializer_class = AutismoSerializer
    permission_classes = [permissions.IsAuthenticated]

class DiagnosticoListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = DiagnosticoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Diagnostico.objects.filter(nino=self.kwargs['nino_id'])

    def perform_create(self, serializer):
        serializer.save(nino_id=self.kwargs['nino_id'])

class DetonanteCrisisListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = DetonanteCrisisSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return DetonanteCrisis.objects.filter(nino=self.kwargs['nino_id'])

    def perform_create(self, serializer):
        serializer.save(nino_id=self.kwargs['nino_id'])

class DebilidadListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = DebilidadSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Debilidad.objects.filter(nino=self.kwargs['nino_id'])

    def perform_create(self, serializer):
        serializer.save(nino_id=self.kwargs['nino_id'])

# Nuevas vistas
class HitoDesarrolloListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = HitoDesarrolloSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return HitoDesarrollo.objects.filter(nino=self.kwargs['nino_id'])

    def perform_create(self, serializer):
        serializer.save(nino_id=self.kwargs['nino_id'])

class ControlEsfinteresRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    serializer_class = ControlEsfinteresSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return ControlEsfinteres.objects.filter(nino=self.kwargs['nino_id'])

class AlimentacionRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    serializer_class = AlimentacionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Alimentacion.objects.filter(nino=self.kwargs['nino_id'])

class SuenoRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    serializer_class = SuenoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Sueno.objects.filter(nino=self.kwargs['nino_id'])

class SensibilidadSensorialListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = SensibilidadSensorialSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return SensibilidadSensorial.objects.filter(nino=self.kwargs['nino_id'])

    def perform_create(self, serializer):
        serializer.save(nino_id=self.kwargs['nino_id'])

class ActividadExtracurricularListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = ActividadExtracurricularSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return ActividadExtracurricular.objects.filter(nino=self.kwargs['nino_id'])

    def perform_create(self, serializer):
        serializer.save(nino_id=self.kwargs['nino_id'])

class AutorizacionRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    serializer_class = AutorizacionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Autorizacion.objects.filter(nino=self.kwargs['nino_id'])