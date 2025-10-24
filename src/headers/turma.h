#ifndef TURMA_H
#define TURMA_H

typedef struct {
    int id;
    char nome[50];
    int professorId;
} Turma;

void listarTurmas();
void cadastrarTurma();
void editarTurma();
void excluirTurma();
void relatorioTurma();

#endif