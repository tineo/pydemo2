from datetime import datetime

from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializers import *
from django.shortcuts import get_object_or_404
from django.db.models import Q

class TransaccionList(generics.ListCreateAPIView):
    lookup_field = 'idtransaccion'
    queryset = Transaccion.objects.all()
    serializer_class = TransaccionSerializer

class TransaccionNew(generics.ListCreateAPIView):
    serializer_class = TransaccionSerializer

    def get_queryset(self):
        cuenta_remitente = self.request.query_params.get('cuenta_remitente')
        cuenta_receptor = self.request.query_params.get('cuenta_receptor')
        monto = self.request.query_params.get('monto')
        nombretransaccion = 'TRANSF'
        tipo = self.request.query_params.get('tipo')
        t1 = Transaccion(cuenta_remitente=cuenta_remitente,
                         cuenta_receptor=cuenta_receptor,
                         monto=monto,
                         nombretransaccion='RET',
                         tipo=1)

        t2 = Transaccion(cuenta_remitente=cuenta_receptor,
                         cuenta_receptor=cuenta_remitente,
                         monto=monto,
                         nombretransaccion='DEP',
                         tipo=2)
        # Transaccion.objects.bulk_create([t1, t2])
        res = Transaccion.objects.bulk_create([t2, t1])
        serializer = self.get_serializer(res)

        # {'email': 'lei
        # headers = self.get_success_headers(serializer.data)
        return Response(Transaccion.objects.all().count())

    def create(self, request, *args, **kwargs):

        cuenta_remitente = request.data['cuenta_remitente']
        cuenta_receptor = request.data['cuenta_receptor']

        monto = request.data['monto']
        nombretransaccion = 'TRANSF'
        tipo = request.data['tipo']

        t1 = Transaccion(cuenta_remitente=cuenta_remitente,
                         cuenta_receptor=cuenta_receptor,
                         monto=monto,
                         nombretransaccion='RET',
                         tipo=1)

        t2 = Transaccion(cuenta_remitente=cuenta_receptor,
                         cuenta_receptor=cuenta_remitente,
                         monto=monto,
                         nombretransaccion='DEP',
                         tipo=2)
        # Transaccion.objects.bulk_create([t1, t2])
        res = Transaccion.objects.bulk_create([t2, t1])
        serializer = self.get_serializer(res)


        # {'email': 'lei
        #headers = self.get_success_headers(serializer.data)
        return Response( Transaccion.objects.all().count())

        # return Transaccion.objects.filter(Q(cuenta_remitente=cuenta) | Q(cuenta_receptor=cuenta))

class TransaccionByCliente(generics.ListAPIView):
    serializer_class = TransaccionSerializer
    def get_queryset(self):
        cuenta = self.request.query_params.get('cuenta')
        return Transaccion.objects.filter((Q(tipo=1) & Q(cuenta_remitente=cuenta)) | (Q(tipo=2) & Q(cuenta_receptor=cuenta))).order_by('-idtransaccion')


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

class CuentaList(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cuenta.objects.all()
    serializer_class = CuentaSerializer

    def get_object(self):
        queryset = self.queryset
        obj = get_object_or_404(
            queryset,
            pk=self.kwargs['pk'],
        )
        return obj

    def retrieve(self, request, pk=None):
        queryset = Cuenta.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = CuentaSerializer(user)
        return Response(serializer.data)

class CuentaNumber(generics.ListAPIView):
    serializer_class = CuentaSerializer
    def get_queryset(self):
        numero = self.request.query_params.get('numero')
        return Cuenta.objects.filter(numerocuenta=numero)

class CuentaByUserId(generics.ListAPIView):
    serializer_class = CuentaSerializer
    def get_queryset(self):
        idusuario = self.request.query_params.get('idusuario')
        return Cuenta.objects.filter(idusuario=idusuario)




class Login(generics.ListAPIView):
    serializer_class = UsuarioSerializer
    def get_queryset(self):
        number = self.request.query_params.get('number')
        passw = self.request.query_params.get('pass')
        return Usuario.objects.filter(Q(usuario=number) | Q(pass_field=passw))


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