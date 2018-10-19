from rest_framework import generics
from .models import *
from .serializers import *
from django.shortcuts import get_object_or_404

class TransaccionList(generics.ListCreateAPIView):
    queryset = Transaccion.objects.all()
    serializer_class = TransaccionSerializer

    def get_object(self):
        queryset = self.queryset
        obj = get_object_or_404(
            queryset,
            pk=self.kwargs['pk'],
        )
        return obj

class BancoList(generics.ListCreateAPIView):
    queryset = Banco.objects.all()
    serializer_class = BancoSerializer

    def get_object(self):
        queryset = self.queryset
        obj = get_object_or_404(
            queryset,
            pk=self.kwargs['pk'],
        )
        return obj

class CuentaList(generics.ListCreateAPIView):
    queryset = Cuenta.objects.all()
    serializer_class = CuentaSerializer

    def get_object(self):
        queryset = self.queryset
        obj = get_object_or_404(
            queryset,
            pk=self.kwargs['pk'],
        )
        return obj

class UsuarioList(generics.ListCreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

    def get_object(self):
        queryset = self.queryset
        obj = get_object_or_404(
            queryset,
            pk=self.kwargs['pk'],
        )
        return obj