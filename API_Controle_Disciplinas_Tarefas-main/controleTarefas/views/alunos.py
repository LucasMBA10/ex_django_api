from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from controleTarefas.models.alunos import AlunosEntidade
from controleTarefas.serializers.alunos import AlunosSerializer

class AlunosView(APIView):

    # método GET busca informações sobre todos os alunos
    def get(self, request, pk=None):
        alunos = AlunosEntidade.objects.all()
        serializer = AlunosSerializer(alunos, many=True)
        return Response(serializer.data)

    # método POST cria um novo aluno
    def post(self, request, format=None):
        serializer = AlunosSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)