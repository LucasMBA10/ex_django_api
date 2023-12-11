from django.contrib import admin
from django.urls import path
from controleTarefas.views.alunos import AlunosView
from controleTarefas.views.alunosDetail import AlunosDetailView
from controleTarefas.views.disciplinas import DisciplinasView
from controleTarefas.views.disciplinasDetail import DisciplinasDetailView
from controleTarefas.views.tarefas import TarefasView
from controleTarefas.views.tarefasDetail import TarefasDetailView
from controleTarefas.views.tarefaAluno import TarefaAlunoView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/alunos/',AlunosView.as_view()),
    path('api/alunos/<int:pk>/',AlunosDetailView.as_view()),
    path('api/disciplinas/', DisciplinasView.as_view()),
    path('api/disciplinas/<int:pk>/',DisciplinasDetailView.as_view()),
    path('api/tarefas/', TarefasView.as_view()),
    path('api/tarefas/<int:pk>/',TarefasDetailView.as_view()),
    path('api/alunos/<int:pk>/tarefas/', TarefaAlunoView.as_view()),
]
