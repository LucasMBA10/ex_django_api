from django.db import models

class AlunosEntidade(models.Model):
    #define campos nome e email
    nome = models.CharField(max_length=100)
    email = models.CharField(max_length=200, unique=True)

    #construtor string
    def __str__(self) -> str:
        return "Alunos [%i- %s]" % (self.id, self.nome)