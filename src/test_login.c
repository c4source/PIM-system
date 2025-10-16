#include <stdio.h>
#include "headers/login.h"
#include "headers/utils.h"

int main() {
    int tipoUsuario = realizarLogin();

    if (tipoUsuario == -1) {
        printf("\nSistema encerrado pelo usuário.\n");
        return 0;
    }

    switch (tipoUsuario) {
        case 1:
            printf("\nLogin como ADMIN detectado  OK.\n");
            break;
        case 2:
            printf("\nLogin como PROFESSOR detectado  OK.\n");
            break;
        case 3:
            printf("\nLogin como ALUNO detectado  OK.\n");
            break;
        default:
            printf("\nErro: tipo de usuário desconhecido.\n");
    }

    return 0;
}