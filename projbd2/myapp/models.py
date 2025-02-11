# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

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
    pnome_funcionario = models.CharField(max_length=10)
    unome_funcionario = models.CharField(max_length=10)
    senha_funcionario = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'funcionario'


class Produto(models.Model):
    id_produto = models.AutoField(primary_key=True)
    nome_produto = models.CharField(max_length=100)
    descricao = models.CharField(max_length=100, blank=True, null=True)
    preco_original = models.DecimalField(max_digits=5, decimal_places=2)
    preco = models.DecimalField(max_digits=5, decimal_places=2)
    id_subcategoria = models.ForeignKey(Categoria, models.DO_NOTHING, db_column='id_subcategoria', blank=True, null=True)
    quantidade = models.IntegerField(blank=True, null=True)
    
    def to_dict(self):
        return {
            'id_produto': self.id_produto,
            'nome_produto': self.nome_produto,
            'preco_produto': str(self.preco),  # Alterando para 'preco', o campo correto
        }
    class Meta:
        managed = False
        db_table = 'produto'


class Promo(models.Model):
    id_promo = models.AutoField(primary_key=True)
    id_produto = models.ForeignKey(Produto, models.DO_NOTHING, db_column='id_produto')
    data_inicio = models.DateField()
    data_fim = models.DateField()
    desconto = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'promo'

import mongoengine as me

class ProdutoImagem(me.Document):
    imagens = me.BinaryField(required=True)  # Para armazenar a imagem em formato binário
    id_prodref = me.IntField(required=True)  # ID de referência do produto no PostgreSQL

    meta = {'collection': 'Images'}  # Define a coleção no MongoDB


class ProdutoVenda(me.EmbeddedDocument):
    produto_id = me.StringField(required=True)
    nome_produto = me.StringField(required=True)
    quantidade = me.IntField(required=True, min_value=1)
    valor_unitario = me.FloatField(required=True, min_value=0.0)
    valor_total = me.FloatField(required=True, min_value=0.0)


class Venda(me.Document):
    produtos = me.EmbeddedDocumentListField(ProdutoVenda)
    data_venda = me.DateTimeField(required=True)
    valor_total_venda = me.FloatField(required=True, min_value=0.0)

    meta = {"collection": "vendas"}  # Define a coleção no MongoDB
