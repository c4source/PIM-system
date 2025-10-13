#ifndef ALUNO_H
#define ALUNO_H

typedef struct {
    int id;
    char nome[100];
    char matricula[20];
} Aluno;

void listarAlunos();
void cadastrarAluno();

#endif
