#ifndef AULA_H
#define AULA_H


typedef struct {
    int id;
    int turmaId;
    int professorId;
    char tema[100];
} Aula;

void listarAulas();
void cadastrarAula();
void editarAula();
void excluirAula();

#endif
