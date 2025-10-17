#ifndef TURMA_H
#define TURMA_H

typedef struct {
    int id;
    char nome[50];
    int alunos[50]; // IDs dos alunos
    int qtdAlunos;
} Turma;

void listarTurmas();
void cadastrarTurma();
void editarTurma();
void excluirTurma();

#endif