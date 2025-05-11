from django.contrib import admin
from .models import *

# i) Ocupação e pessoas
class EstudanteInline(admin.TabularInline):
    model = Estudante
    extra = 1

class ProfessorInline(admin.TabularInline):
    model = Professor
    extra = 1

# ii) Instituição e cursos
class CursoInline(admin.TabularInline):
    model = Curso
    extra = 1

# iii) Área do saber e cursos
class AreaDoSaberInline(admin.TabularInline):
    model = Curso
    fk_name = 'area_saber'  # Ajuste o campo de relacionamento, se necessário
    extra = 1

# iv) Cursos e disciplinas
class DisciplinaInline(admin.TabularInline):
    model = Disciplina
    extra = 1

# v) Disciplinas e avaliações
class AvaliacaoInline(admin.TabularInline):
    model = Avaliacao
    extra = 1

# vi) Turmas e alunos
class MatriculaInline(admin.TabularInline):
    model = Matricula
    extra = 1

# vii) UF e cidades
class CidadeInline(admin.TabularInline):
    model = Cidade
    extra = 1

# viii) Estudantes, disciplinas, avaliações, frequência
class FrequenciaInline(admin.TabularInline):
    model = Frequencia
    extra = 1

# Admin registrations with inlines
@admin.register(UF)
class UFAdmin(admin.ModelAdmin):
    inlines = [CidadeInline]

@admin.register(Cidade)
class CidadeAdmin(admin.ModelAdmin):
    pass

@admin.register(InstituicaoEnsino)
class InstituicaoEnsinoAdmin(admin.ModelAdmin):
    inlines = [CursoInline]

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    inlines = [DisciplinaInline]

@admin.register(AreaDoSaber)
class AreaDoSaberAdmin(admin.ModelAdmin):
    inlines = [AreaDoSaberInline]

@admin.register(Disciplina)
class DisciplinaAdmin(admin.ModelAdmin):
    inlines = [AvaliacaoInline]

@admin.register(Turma)
class TurmaAdmin(admin.ModelAdmin):
    inlines = [MatriculaInline]

@admin.register(Estudante)
class EstudanteAdmin(admin.ModelAdmin):
    inlines = [FrequenciaInline]

@admin.register(Professor)
class ProfessorAdmin(admin.ModelAdmin):
    pass

@admin.register(Ocorrencia)
class OcorrenciaAdmin(admin.ModelAdmin):
    pass

@admin.register(TipoAvaliacao)
class TipoAvaliacaoAdmin(admin.ModelAdmin):
    pass

# Register remaining models without inlines
admin.site.register(Matricula)
admin.site.register(Turno)
