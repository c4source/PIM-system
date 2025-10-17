#ifndef ATIVIDADE_H
#define ATIVIDADE_H

typedef struct{
    int id;
    char titulo[30];
    char descricao[100];
    int turmaId;
    int aulaId;
    double nota;
    char status[10];
} Atividade;


void listarAtividades();
void cadastrarAtividade();
void editarAtividade();
void excluirAtividade();

#endif
