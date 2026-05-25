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
    views = models.IntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return f"{self.icone} {self.nome}"


class Comentario(models.Model):
    vulnerabilidade = models.ForeignKey(
        Vulnerabilidade,
        on_delete=models.CASCADE,
        related_name='comentarios'
    )

    autor = models.CharField(
        max_length=100,
        blank=True,
        default='Anónimo'
    )

    texto = models.TextField()
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comentário de {self.autor} em {self.vulnerabilidade.nome}"


class SugestaoVulnerabilidade(models.Model):
    RISCO_CHOICES = [
        ('A', 'Alto'),
        ('M', 'Médio'),
        ('B', 'Baixo'),
        ('', 'Não sei'),
    ]

    nome = models.CharField(max_length=100)
    descricao = models.TextField()

    risco = models.CharField(
        max_length=1,
        choices=RISCO_CHOICES,
        blank=True
    )

    mitigacao = models.TextField(blank=True)
    email_contacto = models.EmailField(blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Sugestão: {self.nome}"