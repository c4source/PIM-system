#ifndef ALUNO_H
#define ALUNO_H

typedef struct {
    int id;
    char nome[100];
    char email[50];
    char senha[20];
} Aluno;

void listarAlunos();
void cadastrarAluno();
void editarAluno();
void excluirAluno();

#endif
