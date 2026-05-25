from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.http import JsonResponse
from .models import Vulnerabilidade, Comentario, SugestaoVulnerabilidade

def home(request):
    context = {
        'total_vulnerabilidades': Vulnerabilidade.objects.count(),
        'total_comentarios': Comentario.objects.count(),
        'total_sugestoes': SugestaoVulnerabilidade.objects.count(),
    }
    return render(request, 'social/home.html', context)

def lista_vulnerabilidades(request):
    qs = Vulnerabilidade.objects.all()
    q = request.GET.get('q')
    risco = request.GET.get('risco')
    if q:
        qs = qs.filter(Q(nome__icontains=q) | Q(descricao__icontains=q))
    if risco:
        qs = qs.filter(risco=risco)
    qs = qs.order_by('risco', 'nome')
    if q and not qs.exists():
        return redirect(f'/nao-encontrado/?q={q}')
    return render(request, 'social/lista.html', {'vulnerabilidades': qs})

def detalhe(request, id):
    vuln = get_object_or_404(Vulnerabilidade, id=id)
    vuln.views += 1
    vuln.save(update_fields=['views'])
    if request.method == 'POST':
        autor = request.POST.get('autor', 'Anónimo').strip()
        texto = request.POST.get('texto', '').strip()
        if texto:
            Comentario.objects.create(
                vulnerabilidade=vuln,
                autor=autor if autor else 'Anónimo',
                texto=texto
            )
        return redirect('detalhe', id=vuln.id)
    comentarios = vuln.comentarios.all().order_by('-criado_em')
    return render(request, 'social/detalhe.html', {'vuln': vuln, 'comentarios': comentarios})

def ranking(request):
    alto_qs = Vulnerabilidade.objects.filter(risco='A').order_by('-views', '-created_at')
    medio_qs = Vulnerabilidade.objects.filter(risco='M').order_by('-views', '-created_at')
    baixo_qs = Vulnerabilidade.objects.filter(risco='B').order_by('-views', '-created_at')
    alto_max = alto_qs.first().views if alto_qs else 0
    medio_max = medio_qs.first().views if medio_qs else 0
    baixo_max = baixo_qs.first().views if baixo_qs else 0
    ranking_data = [
        {'cor': 'red',   'titulo': '🔴 Risco Alto',   'rank_list': alto_qs,   'max_views': alto_max},
        {'cor': 'yellow','titulo': '🟠 Risco Médio',  'rank_list': medio_qs,  'max_views': medio_max},
        {'cor': 'green', 'titulo': '🟢 Risco Baixo',  'rank_list': baixo_qs,  'max_views': baixo_max},
    ]
    return render(request, 'social/ranking.html', {'ranking_data': ranking_data})

def about(request):
    return render(request, 'social/about.html')

def sugestoes(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        descricao = request.POST.get('descricao')
        risco = request.POST.get('risco', '')
        mitigacao = request.POST.get('mitigacao', '')
        email = request.POST.get('email', '')
        if nome and descricao:
            SugestaoVulnerabilidade.objects.create(
                nome=nome,
                descricao=descricao,
                risco=risco,
                mitigacao=mitigacao,
                email_contacto=email
            )
            return redirect('sugestoes')
    sugestoes_lista = SugestaoVulnerabilidade.objects.all().order_by('-criado_em')
    return render(request, 'social/sugestoes.html', {'sugestoes': sugestoes_lista})

def api_sugestao_nomes(request):
    termo = request.GET.get('q', '')
    if len(termo) < 1:
        return JsonResponse([], safe=False)
    nomes = Vulnerabilidade.objects.filter(nome__istartswith=termo).values_list('nome', flat=True)[:10]
    return JsonResponse(list(nomes), safe=False)

def nao_encontrado(request):
    termo = request.GET.get('q', '')
    return render(request, 'social/nao_encontrado.html', {'termo': termo})

def register_error(request):
    return render(request, 'registration/register_error.html')