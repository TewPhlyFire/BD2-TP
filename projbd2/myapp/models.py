# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Caixa(models.Model):
    id_caixa = models.AutoField(primary_key=True)
    saldo = models.DecimalField(max_digits=100, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'caixa'


class Categoria(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    id_subcategoria = models.ForeignKey('self', models.DO_NOTHING, db_column='id_subcategoria', blank=True, null=True)
    nome_categoria = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'categoria'


class Cliente(models.Model):
    nif_cliente = models.IntegerField(primary_key=True)
    pnome_cliente = models.CharField(max_length=10)
    unome_cliente = models.CharField(max_length=10)
    contacto_tel = models.CharField(max_length=20)
    morada = models.CharField(max_length=50)
    mail = models.CharField(max_length=50)
    password_client = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'cliente'


class Funcionario(models.Model):
    id_funcionario = models.AutoField(primary_key=True)
    pnome_funcionario = models.CharField(max_length=255)
    unome_funcionario = models.CharField(max_length=255)
    senha_funcionario = models.CharField(max_length=255)

    def __str__(self):
        return self.pnome_funcionario

class Pedido(models.Model):
    id_pedido = models.AutoField(primary_key=True)
    id_produto = models.ForeignKey('Produto', models.DO_NOTHING, db_column='id_produto')
    data_hora = models.DateTimeField(blank=True, null=True)
    quantidade = models.IntegerField()
    total = models.DecimalField(max_digits=5, decimal_places=2)
    nif_cliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='nif_cliente', blank=True, null=True)
    id_funcionario = models.ForeignKey(Funcionario, models.DO_NOTHING, db_column='id_funcionario', blank=True, null=True)
    id_caixa = models.ForeignKey(Caixa, models.DO_NOTHING, db_column='id_caixa', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pedido'


class Produto(models.Model):
    id_produto = models.AutoField(primary_key=True)
    nome_produto = models.CharField(max_length=100)
    descricao = models.CharField(max_length=100)
    preco_produto = models.DecimalField(max_digits=5, decimal_places=2)
    id_subcategoria = models.ForeignKey(Categoria, models.DO_NOTHING, db_column='id_subcategoria', blank=True, null=True)
    quantidade = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'produto'
