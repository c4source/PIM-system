#ifndef PROFESSOR_H
#define PROFESSOR_H

typedef struct {
    int id;
    char nome[100];
    char email[50];
    char senha[20];
} Professor;

void listarProfessores();
void cadastrarProfessor();
void editarProfessor();
void excluirProfessor();

#endif