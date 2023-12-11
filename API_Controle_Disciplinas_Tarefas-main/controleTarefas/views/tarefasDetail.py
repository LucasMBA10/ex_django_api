from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from controleTarefas.models.tarefas import TarefasEntidade
from controleTarefas.serializers.tarefas import TarefasSerializer

class TarefasDetailView (APIView):

    # método GET para obter uma tarefa expecifico pelo seu ID(pk)
    def get_object(self, pk):
        try:
            return TarefasEntidade.objects.get(pk=pk)
        except TarefasEntidade.DoesNotExist:
            raise Http404

    # método GET para buscar as informações da tarefa
    def get(self, request, pk, format=None):
        tarefas = self.get_object(pk)
        serializer = TarefasSerializer(tarefas)
        return Response(serializer.data)

    # método PUT atualiza todas as informacoes de uma tarefa existente
    def put(self, request, pk, format=None):
        tarefas = self.get_object(pk)        
        serializer = TarefasSerializer(tarefas,data=request.data)
         # salva as alterações se os dados forem válidos
        if (serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # método DELETE exclui uma tarefa expecifica
    def delete(self, request, pk, format=None):
        tarefas = self.get_object(pk)
        tarefas.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)