#include <stdio.h>
#include <string.h>   //Cabeçalho para manipulação de strings
#include "admin.h"    

Administrador admin[MAX_ADM]; // Repositório de dados de administradores 
int totalAdmin = 0;   // Contador de administradores cadastrados

 void cadastrarAdministrador(void) {
    if (totalAdmin >= MAX_ADM) {
        printf("Limite de administradores atingido. \n");
        return;
    }
 
    Administrador adm; // Coleta de nome, login e senha --> typedef struct 

    printf("Digite o nome do administrador: ");
    fgets(adm.nome, MAX_STR, stdin);
    adm.nome[strcspn(adm.nome, "\n")] = '\0';

    printf("Digite o login: ");
    fgets(adm.login, MAX_STR, stdin);
    adm.login[strcspn(adm.login, "\n")] = '\0';

    printf("Digite a senha: ");
    fgets(adm.senha, MAX_STR, stdin);
    adm.senha[strcspn(adm.senha, "\n")] = '\0';

    admin[totalAdmin++] = adm;

    printf("Administrador cadastrado com sucesso!\n");
}

void listarAdministrador(void) {
    if (totalAdmin == 0) {
        printf("Nenhum administrador cadastrado. \n");   
        return;
    }

    printf("\n--- Lista de administradores  ---\n");
    for (int i = 0; i < totalAdmin; i++) {
        printf("Nome: %s | Login: %s\n", admin[i].nome, admin[i].login);
    }

}
// Menu de administrador//
void menuAdministrador(void) {
    int opcao; 

    do { 
        LimparTela();
        printf("\n== MENU DO ADMINISTRADOR ==\n");
        printf("1. Cadastrar Administrador\n");
        printf("2. Listar Administradores\n");
        printf("0. Sair\n");
        printf("Opcao desejada: ");
        
        if (scanf("%d", &opcao) != 1) {
            opcao = -1; // Define uma opção inválida
        }
    }   while (getchar() != '\n');
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
            }   
}