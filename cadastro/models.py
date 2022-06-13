from operator import length_hint
from django.db import models
from django.contrib.auth.models import User
from django import forms


# Create your models here.
class aluno(models.Model):
    
    nome_aluno = models.CharField(max_length=200)
    cpf_aluno = models.IntegerField
    end_aluno = models.CharField(max_length=200)
    escola = models.CharField(max_length=200)
    end_escola = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.aluno.url


class escola(models.Model):
    escola = models.CharField(max_length=200)
    cnpj = models.IntegerField
    endereco = models.CharField(max_length=200)
    telefone = models.IntegerField
    responsavel = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.escolas.url


class responsavel(models.Model):
    nome_resp = models.CharField(max_length=200)
    cpf_resp = models.IntegerField
    end_resp = models.CharField(max_length=200)
    tel_resp = models.IntegerField
    
    def __str__(self) -> str:
        return self.resposavel.url


class transportador(models.Model):
    nome_transp = models.CharField(max_length=200)
    cpf_transp = models.IntegerField
    end_transp = models.CharField(max_length=200)
    tel_transp = models.IntegerField
    veiculo = models.CharField(max_length=200)
    placa = models.CharField(max_length=7)
    capacidade = models.IntegerField
    tempo_atua = models.IntegerField
    escola_atende = models.CharField(max_length=1000)

    def __str__(self) -> str:
        return self.transportador.ur


class rota(models.Model):
    nome_transp = models.CharField
    rota = models.ManyToManyField

