# Generated by Django 4.2.5 on 2023-09-21 13:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('controleTarefas', '0002_rename_descrição_disciplinasentidade_descricao_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tarefasentidade',
            old_name='AlunosTarefas',
            new_name='alunosTarefas',
        ),
        migrations.RenameField(
            model_name='tarefasentidade',
            old_name='DisiplinasTarefas',
            new_name='disciplinasTarefas',
        ),
    ]
