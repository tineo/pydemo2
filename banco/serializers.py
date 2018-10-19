from .models import *
from rest_framework import serializers

class TransaccionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Transaccion
        fields = ('idtransaccion', 'monto', 'fecha', 'nombreTransaccion', 'tipo', 'cuenta_remitente', 'cuenta_receptor')


class BancoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Banco
        fields = ('idbancos', 'nombrebanco')


class CuentaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cuenta
        fields = ('idcuenta', 'nombreCuenta', 'monto', 'idusuario', 'idbancos')

class UsuarioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Usuario
        fields = ('idusuario', 'nombre', 'apellido', 'usuario', 'pass')