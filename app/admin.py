from django.contrib import admin
from .models import *

class EstudanteInline(admin.TabularInline):
    model = Estudante
    extra = 1

class ProfessorInline(admin.TabularInline):
    model = Professor
    extra = 1

class CursoInline(admin.TabularInline):
    model = Curso
    extra = 1


class AreaDoSaberInline(admin.TabularInline):
    model = Curso
    fk_name = 'area_saber'  
    extra = 1


class DisciplinaInline(admin.TabularInline):
    model = Disciplina
    extra = 1

class AvaliacaoInline(admin.TabularInline):
    model = Avaliacao
    extra = 1


class MatriculaInline(admin.TabularInline):
    model = Matricula
    extra = 1


class CidadeInline(admin.TabularInline):
    model = Cidade
    extra = 1


class FrequenciaInline(admin.TabularInline):
    model = Frequencia
    extra = 1


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
    inlines = [DisciplinaInline, FrequenciaInline]

@admin.register(AreaDoSaber)
class AreaDoSaberAdmin(admin.ModelAdmin):
    inlines = [AreaDoSaberInline]

@admin.register(Disciplina)
class DisciplinaAdmin(admin.ModelAdmin):
    inlines = [AvaliacaoInline, FrequenciaInline]


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

@admin.register(Avaliacao)
class AvaliacaoAdmin(admin.ModelAdmin):
    list_display = ('descricao_curta', 'curso', 'disciplina', 'tipo_avaliacao', 'nota')
    list_filter = ('curso', 'disciplina', 'tipo_avaliacao')
    search_fields = ('descricao', 'disciplina__nome', 'curso__nome')
    
    def descricao_curta(self, obj):
        return obj.descricao[:50] + ('...' if len(obj.descricao) > 50 else '')
    
    descricao_curta.short_description = 'Descrição'


admin.site.register(Matricula)
admin.site.register(Turno)

@admin.register(Frequencia)
class FrequenciaAdmin(admin.ModelAdmin):
    list_display = ('pessoa', 'curso', 'disciplina', 'numero_faltas')
    list_filter = ('curso', 'disciplina')
    search_fields = ('pessoa__nome', 'disciplina__nome', 'curso__nome')
