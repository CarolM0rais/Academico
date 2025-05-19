from django.shortcuts import render
from .models import *


def IndexView(request):
    return render(request, 'index.html')

def EstudantesView(request):
    context = {
        'estudantes': Estudante.objects.all(),
    }

    return render(request, 'estudantes.html', context)

def TurmasView(request):
    context = {
        'turmas': Turma.objects.all(),
    }
    return render(request, 'turmas.html', context)

def DisciplinasView(request):
    context = {
        'disciplinas': Disciplina.objects.all(),
    }
    return render(request, 'disciplinas.html', context)

def CursosView(request):
    context = {
        'cursos': Curso.objects.all(),
    }
    return render(request, 'cursos.html', context)

def AvaliacoesView(request):
    context = {
        'avaliacoes': Avaliacao.objects.all(),
    }
    return render(request, 'avaliacoes.html', context)

def ProfessoresView(request):
    context = {
        'professores': Professor.objects.all(),
    }
    return render(request, 'professores.html', context)

def FrequenciasView(request):
    context = {
        'frequencia': Frequencia.objects.all(),
    }
    return render(request, 'frequencia.html', context)

def MatriculasView(request):
    context = {
        'matriculas': Matricula.objects.all(),
    }
    return render(request, 'matriculas.html', context)

def OcorrenciasView(request):
    context = {
        'ocorrencias': Ocorrencia.objects.all(),
    }
    return render(request, 'ocorrencias.html', context)

def InstituicoesView(request):
    context = {
        'instituicoes': InstituicaoEnsino.objects.all(),
    }
    return render (request, 'instituicoes.html', context)

def AreasdosaberView(request):
    context = {
        'areasdosaber': AreaDoSaber.objects.all(),
    }
    return render (request, 'areadosaber.html', context)    