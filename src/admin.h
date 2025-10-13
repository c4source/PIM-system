#ifndef ADMIN_H
#define ADMIN_H

#define MAX_ADM 100
#define MAX_STR 10 

typedef struct {

    char nome[MAX_STR];
    char login[MAX_STR]; 
    char senha[MAX_STR]; // No futuro, criptografia
} Administrador;

void cadastrarAdministrador();
void listarAdminstrador();

#endif