#include <stdio.h>
#include "admin.h"

int main(void) { 
    int opcao;

    do {
        printf("\n=== MENU ADMIN ===\n");
        printf("1. Cadastrar Administrador\n");
        printf("2. Listar Administradores\n");
        printf("0. Sair\n");
        printf("Opcao desejada: ");

        if (scanf("%d", &opcao) != 1) {
            opcao = -1; // Define uma opção inválida
        } 

        while (getchar() != '\n');
            switch (opcao){
                case 1:
                    cadastrarAdministrador();
                    break;
                case 2:
                    listarAdministrador();
                    break;
                case 0:
                    printf("Saindo... \n");
                    break;
                default:
                    printf("Opcao invalida. Tente novamente. \n");   

            }   
    
    } while( opcao != 0 );

    return 0;
}