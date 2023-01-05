from apiproyecto.models import Alumnos, Carreras, PeriodosEscolares, Personal
from rest_framework import viewsets, permissions
from .serializers import AlumnosSerializers, PersonalSerializers, PeriodosEscolaresSerializers, CarrerasSerializers

class AlumnosViewSet(viewsets.ModelViewSet):
    queryset = Alumnos.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = AlumnosSerializers

class PersonalViewSet(viewsets.ModelViewSet):
    queryset = Personal.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = PersonalSerializers

class PeriodosEscolaresViewSet(viewsets.ModelViewSet):
    queryset = PeriodosEscolares.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = PeriodosEscolaresSerializers

class CarrerasViewSet(viewsets.ModelViewSet):
    queryset = Carreras.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = CarrerasSerializers