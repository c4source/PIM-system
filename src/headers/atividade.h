#ifndef ATIVIDADE_H
#define ATIVIDADE_H

typedef struct{
    int id;
    char titulo[30];
    char descricao[100];
    int turmaId;
    int aulaId;
} Atividade;


void listarAtividades();
void cadastrarAtividade();
void editarAtividade();
void excluirAtividade();

#endif
