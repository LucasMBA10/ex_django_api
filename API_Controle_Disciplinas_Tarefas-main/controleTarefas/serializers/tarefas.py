from rest_framework import serializers
from controleTarefas.models.tarefas import TarefasEntidade

class TarefasSerializer(serializers.ModelSerializer):
    class Meta:
        model = TarefasEntidade
        fields = '__all__'