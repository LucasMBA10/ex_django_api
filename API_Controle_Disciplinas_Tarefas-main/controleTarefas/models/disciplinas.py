from django.db import models

class DisciplinasEntidade(models.Model):
    #define campos nome e descrição
    nome = models.CharField(max_length=70)
    descricao = models.TextField()

    #construtor string
    def __str__(self) -> str:
        return "Dispiplina [%i - %s]" % (self.id, self.nome)