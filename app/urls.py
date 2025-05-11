from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView, name='index'),
    path('estudantes', views.EstudantesView, name='estudantes'),
    path('turmas', views.TurmasView, name='turmas'),
    path('disciplinas', views.DisciplinasView, name='disciplinas'),
    path('cursos', views.CursosView, name='cursos'),
    path('avaliacoes', views.AvaliacoesView, name='avaliacoes'),
    path('professores', views.ProfessoresView, name='professores'),
    path('frequencia', views.FrequenciasView, name='frequencia'),
    path('matriculas', views.MatriculasView, name='matriculas'),
    path('ocorrencias', views.OcorrenciasView, name='ocorrencias'),
    path('instituicoes', views.InstituicoesView, name='instituicoes'),
    path('areasdosaber', views.AreasdosaberView, name='areasdosaber'),
]