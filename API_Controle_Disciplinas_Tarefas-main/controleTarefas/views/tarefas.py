from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from controleTarefas.models.tarefas import TarefasEntidade
from controleTarefas.serializers.tarefas import TarefasSerializer

class TarefasView(APIView):

    # método GET busca informações sobre todos as tarefas
    def get(self, request, pk=None):
        tarefas = TarefasEntidade.objects.all()
        serializer = TarefasSerializer(tarefas, many=True)
        return Response(serializer.data)

    # método POST cria uma nova tarefa
    def post(self, request, format=None):
        serializer = TarefasSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    