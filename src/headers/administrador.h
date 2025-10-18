#ifndef ADMINISTRADOR_H
#define ADMINISTRADOR_H

typedef struct administrador
{
    int id;
    char nome[100];
    char email[50];
    char senha[20];
}Administrador;

void cadastrarAdministrador();
void editarAdministrador();
void excluirAdministrador();
void listarAdministradores();


#endif