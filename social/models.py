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
    icone = models.CharField(max_length=10, default='🛡️')
    views = models.IntegerField(default=0)          # Campo necessário para o ranking
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.icone} {self.nome}"