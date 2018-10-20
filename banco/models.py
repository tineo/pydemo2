from datetime import datetime

from django.db import models

# Create your models here.
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.

class Banco(models.Model):
    idbancos = models.AutoField(primary_key=True)
    nombrebanco = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'banco'


class Cuenta(models.Model):
    idcuenta = models.AutoField(primary_key=True)
    numerocuenta = models.CharField(db_column='numeroCuenta', max_length=45, blank=True, null=True)  # Field name made lowercase.
    monto = models.FloatField(blank=True, null=True)
    idusuario = models.IntegerField()
    idbancos = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cuenta'


class Transaccion(models.Model):
    idtransaccion = models.AutoField(primary_key=True)
    monto = models.FloatField(blank=True, null=True)
    fecha = models.DateTimeField(blank=True, default=datetime.now)
    nombretransaccion = models.CharField(db_column='nombreTransaccion', max_length=15, blank=True, null=True)  # Field name made lowercase.
    tipo = models.IntegerField(blank=True, null=True)
    cuenta_remitente = models.IntegerField()
    cuenta_receptor = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'transaccion'


class Usuario(models.Model):
    idusuario = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=15, blank=True, null=True)
    apellido = models.CharField(max_length=25, blank=True, null=True)
    usuario = models.CharField(max_length=15)
    pass_field = models.CharField(db_column='pass', max_length=15)  # Field renamed because it was a Python reserved word.

    class Meta:
        managed = False
        db_table = 'usuario'
