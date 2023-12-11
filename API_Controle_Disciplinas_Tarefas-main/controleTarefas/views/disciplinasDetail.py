from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from controleTarefas.models.disciplinas import DisciplinasEntidade
from controleTarefas.serializers.disciplinas import DisciplinasSerializer

class DisciplinasDetailView (APIView):

    # método GET para obter uma disciplina expecifico pelo seu ID(pk)
    def get_object(self, pk):
        try:
            return DisciplinasEntidade.objects.get(pk=pk)
        except DisciplinasEntidade.DoesNotExist:
            raise Http404

    # método GET para buscar as informações da disciplina
    def get(self, request, pk, format=None):
        disciplinas = self.get_object(pk)
        serializer = DisciplinasSerializer(disciplinas)
        return Response(serializer.data)

    # método PUT atualiza todas as informacoes de uma disciplina existente
    def put(self, request, pk, format=None):
        disciplinas = self.get_object(pk)        
        serializer = DisciplinasSerializer(disciplinas,data=request.data)
         # salva as alterações se os dados forem válidos
        if (serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # método DELETE exclui uma disciplina expecifica
    def delete(self, request, pk, format=None):
        disciplinas = self.get_object(pk)
        disciplinas.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)