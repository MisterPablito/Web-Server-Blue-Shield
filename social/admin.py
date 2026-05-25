from django.contrib import admin
from .models import Vulnerabilidade, Comentario, SugestaoVulnerabilidade

@admin.register(Vulnerabilidade)
class VulnerabilidadeAdmin(admin.ModelAdmin):
    list_display = ('nome', 'risco', 'views', 'created_at')
    search_fields = ('nome',)
    list_filter = ('risco',)
    readonly_fields = ('created_at', 'updated_at')
    ordering = ('-created_at',)
    list_per_page = 10

@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('autor', 'vulnerabilidade', 'criado_em')
    list_filter = ('vulnerabilidade',)
    search_fields = ('autor', 'texto')

@admin.register(SugestaoVulnerabilidade)
class SugestaoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'risco', 'criado_em')
    list_filter = ('risco',)
    search_fields = ('nome',)