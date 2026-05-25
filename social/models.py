from django.db import models

class Vulnerabilidade(models.Model):
    RISCO_CHOICES = [
        ('A', 'Alto'),
        ('M', 'Médio'),
        ('B', 'Baixo'),
    ]

    nome = models.CharField(max_length=100, unique=True)
    descricao = models.TextField()
    risco = models.CharField(max_length=1, choices=RISCO_CHOICES)
    mitigacao = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.nome