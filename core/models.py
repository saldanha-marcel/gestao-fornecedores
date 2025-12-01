from django.db import models

class SalesModel(models.Model):
    mes = models.CharField(max_length=12)
    ano = models.IntegerField()
    codigo_empresa = models.IntegerField()
    id_departamento = models.IntegerField()
    id_marca = models.IntegerField()
    id_produto = models.IntegerField()
    quantidade = models.CharField(max_length=50)
    valor_unitario = models.CharField(max_length=50)
    valor_total = models.CharField(max_length=50)
    custo_unitario = models.CharField(max_length=50)
    custo_total = models.CharField(max_length=50)
    markup_multiplicador = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.produto} - {self.empresa} ({self.mes}/{self.ano})"

class produtos(models.Model):
    id_produto = models.AutoField(primary_key=True)
    nome_produto = models.CharField(max_length=100)

    def __str__(self):
        return self.nome_produto

class marcas(models.Model):
    id_marca = models.AutoField(primary_key=True)
    nome_marca = models.CharField(max_length=100)

    def __str__(self):
        return self.nome_marca

class departamentos(models.Model):
    id_departamento = models.AutoField(primary_key=True)
    nome_departamento = models.CharField(max_length=100)

    def __str__(self):
        return self.nome_departamento

class empresas(models.Model):
    codigo_empresa = models.AutoField(primary_key=True)
    nome_empresa = models.CharField(max_length=100)
    nome_fantasia = models.CharField(max_length=100)

    def __str__(self):
        return self.nome_empresa