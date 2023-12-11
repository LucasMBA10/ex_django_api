from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from controleTarefas.models.disciplinas import DisciplinasEntidade
from controleTarefas.serializers.disciplinas import DisciplinasSerializer

class DisciplinasView(APIView):

    # método GET busca informações sobre todos as disciplinas
    def get(self, request, pk=None):
        disciplinas = DisciplinasEntidade.objects.all()
        serializer = DisciplinasSerializer(disciplinas, many=True)
        return Response(serializer.data)

    # método POST cria uma nova disciplina
    def post(self, request, format=None):
        serializer = DisciplinasSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)