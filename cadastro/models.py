from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class aluno(models.Model):
    nome_aluno = models.CharField(max_length=200)
    cpf_aluno = models.IntegerField(max_length=11)
    end_aluno = models.CharField(max_length=200)
    escola_aluno = models.CharField(max_length=200)
    end_escola_aluno = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.aluno.url


class escola(models.Model):
    escola = models.CharField(max_length=200)
    cnpj = models.IntegerField(max_length=14)
    endereco = models.CharField(max_length=200)
    telefone = models.IntegerField(max_length=12)
    responsavel = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.escola.url


class responsavel(models.Model):
    nome_resp = models.CharField(max_length=200)
    cpf_resp = models.IntegerField(max_length=11)
    end_resp = models.CharField(max_length=200)
    tel_resp = models.IntegerField(max_length=12)
    
    def __str__(self) -> str:
        return self.resposavel.url


class transportador(models.Model):
    nome_transp = models.CharField(max_length=200)
    cpf_transp = models.IntegerField(max_length=11)
    end_transp = models.CharField(max_length=200)
    tel_transp = models.IntegerField(max_length=11)
    veiculo = models.CharField(max_length=200)
    placa = models.CharField(max_length=7)
    capacidade = models.IntegerField(max_length=10)
    tempo_atua = models.IntegerField(max_length=5)
    escola_atende = models.CharField(max_length=1000)

    def __str__(self) -> str:
        return self.transportador.url
