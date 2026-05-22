from django.contrib import admin
from .models import Vulnerabilidade

@admin.register(Vulnerabilidade)
class VulnerabilidadeAdmin(admin.ModelAdmin):
    list_display = ('nome', 'risco', 'created_at')
    search_fields = ('nome',)
    list_filter = ('risco',)
    ordering = ('-created_at',)