#ifndef PROFESSOR_H
#define PROFESSOR_H

typedef struct {
    int id;
    char nome[100];
    char matricula[20];
} Professor;

void listarProfessores();
void cadastrarProfessor();

#endif