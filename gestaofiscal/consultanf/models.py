"""
Ao criar os models, devemos pensar nos dados que guardaremos e as relações entre os diferentes modelos.

Sistema de Geração de NF utilizando ORM para mapeamento do DB no Django.

"""
from django.db import models
from django.urls import reverse


class NotaFiscal(models.Model):
    """Classe responsável pelo objeto Nota Fiscal"""

    # Em caso de IntegerField, uma chama primária será automaticamente adicionada ao modelo caso não definamos o contrário
    numero = models.IntegerField()
    valor_bruto = models.IntegerField()
    serie = models.IntegerField()

    #Classes Estrangeiras
    empresa = models.ForeignKey('Empresa', on_delete=models.SET_NULL, null=True)
    item_nf = models.ForeignKey('ItemNF', on_delete=models.SET_NULL, null=True)

    class Meta:
        ordering = ['empresa']

    def __str__(self):
        return f'{self.numero}, {self.empresa}'

    def get_absolute_url(self):
        return reverse('notafiscal-detail', args=[str(self.numero)])

import uuid
class ItemNF(models.Model):

    id=models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='ID único para o item')
    peso = models.IntegerField()
    valor_item = models.IntegerField()
    produto = models.ForeignKey('Produto', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.produto}'

class Empresa(models.Model):
    nome_fantasia = models.CharField(max_length=100)
    razao_social = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=15)

    class Meta:
        ordering = ['razao_social']

    def get_absolute_url(self):
        return reverse('empresa-detail', args=[str(self.razao_social)])

    def __str__(self):
        return f'{self.nome_fantasia}, {self.cnpj}'

class Produto(models.Model):
    nome_produto = models.CharField(max_length=30)
    unidade_produto = models.IntegerField()

    def __str__(self):
        return f'{self.nome_produto}'