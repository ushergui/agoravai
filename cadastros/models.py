from django.db import models
from django.contrib.auth.models import User
#Pra deixar cada um ver somente aquilo que cadastrou, exemplo pra usar: Produtividade

# Create your models here.

class Estado (models.Model):
    nome_estado=models.CharField(max_length=25, verbose_name="Estado")
    sigla_estado=models.CharField(max_length=2, verbose_name="Sigla do Estado")
    #Anotação padrão para informar que é string
    def __str__(self):
        return "{} - {}".format(self.sigla_estado, self.nome_estado)
    class Meta:
        ordering = ['nome_estado']


class Cidade (models.Model):
    nome_cidade=models.CharField(max_length=80, verbose_name="Cidade")
    estado=models.ForeignKey(Estado, on_delete=models.PROTECT)

    def __str__(self):
        return "{} - {}".format(self.nome_cidade, self.estado)

class Bairro (models.Model):
    bairro=models.CharField(max_length=70, verbose_name="Bairro")
    cidade=models.ForeignKey(Cidade, on_delete=models.PROTECT)
    def __str__(self):
        return "{} - {}".format(self.bairro, self.cidade)

class Logradouro (models.Model):
    logradouro=models.CharField(max_length=80, verbose_name="Logradouro")
    bairro=models.ForeignKey(Bairro, on_delete=models.PROTECT)
    cep = models.CharField(max_length=13, verbose_name="CEP")
    def __str__(self):
        return "{} - {} - {}".format(self.logradouro, self.bairro, self.cep)

class Proprietario(models.Model):
    nome_proprietario = models.CharField(max_length=55)
    logradouro_proprietario = models.ForeignKey(Logradouro, on_delete=models.PROTECT)
    numero_proprietario=models.CharField(max_length=20, verbose_name="Número", null=True)
    complemento_proprietario=models.CharField(max_length=40, verbose_name="Complemento", null=True, blank=True)
    def __str__(self):
        return self.nome_proprietario

    @property
    def complemento(self):
        if self.proprietario.complemento_proprietario is not None:
            return self.proprietario.complemento_proprietario


class Terreno(models.Model):
    inscricao = models.CharField(max_length=18, null=False, verbose_name="Inscrição imobiliária")
    logradouro_terreno = models.ForeignKey(Logradouro, on_delete=models.PROTECT, verbose_name="Logradouro do terreno", related_name="logradouro_terreno")
    numero_terreno = models.CharField(max_length=20, verbose_name="Número do terreno")
    complemento_terreno = models.CharField(max_length=40, verbose_name="Complemento")
    proprietario = models.ForeignKey(Proprietario, on_delete=models.PROTECT, verbose_name="Proprietário")
    lote = models.CharField(max_length=4, null=False)
    quadra = models.CharField(max_length=4, null=False)
    area = models.FloatField(null=False)
    logradouro_correspondencia = models.ForeignKey(Logradouro, on_delete=models.PROTECT, verbose_name="Endereço de correspondência", related_name="logradouro_correspondencia")
    numero_correspondencia = models.CharField(max_length=20, verbose_name="Número")
    complemento_correspondencia = models.CharField(max_length=40, verbose_name="Complemento")

    def __str__(self):
        return "{} - {}, {}".format(self.inscricao, self.proprietario, self.area)

class Produtividade(models.Model):
    descricao = models.CharField(max_length=280, null=False, verbose_name="Descrição")
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)
    pdf_teste = models.FileField(upload_to='pdf/')
    # posso usar este models.ForeignKey(User) para saber quem alterou alguma coisa ou criou


