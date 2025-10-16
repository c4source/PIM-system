#include <stdio.h>
#include <string.h>
#include "headers/login.h"  //inclui a definição da função realizarLogin().
#include "headers/utils.h"  //inclui a definição da função LimparTela() e pausar().


 

Usuario usuarios[] = { //Cria um novo tipo de dado 

    {"admin", "1234", ADMIN_ROLE},
    {"professor", "abcd", PROFESSOR_ROLE},
    {"aluno", "4321", ALUNO_ROLE},

};
int totalUsuarios = 3;


int realizarLogin() {
    char login[30];
    char senha[30];
    int tentativas = 0; 

    while(tentativas < MAX_TENTATIVAS) {
        printf("=====================================\n");
        printf("          TELA DE LOGIN\n");
        printf("   (%d tentativas restantes)\n", MAX_TENTATIVAS - tentativas);
        printf("=====================================\n\n");

        printf("Digite seu login: (ou 'sair' para encerrar): ");
        if (fgets(login, sizeof(login), stdin) == NULL) 
            return SAIR_SISTEMA;
       
        login[strcspn(login, "\n")] = '\0';  //Remove o caractere ENTER do final da string  
        
        if (strcmp(login, "sair") == 0) //Verifica se o usuario digitou 'sair' retornando o fim do programa.
            return SAIR_SISTEMA;

        printf("Digite sua senha: ");
        if (fgets(senha, sizeof(senha), stdin) == NULL)
            return SAIR_SISTEMA;
        
        senha[strcspn(senha, "\n")] = '\0';  //Remove o caractere ENTER do final da string 
        
        //Verifica as credenciaias
        for (int i = 0; i < totalUsuarios; i++) {
            if (strcmp(login, usuarios[i].login) == 0 && strcmp(senha, usuarios[i].senha) == 0) {
                
                printf("\nLogin bem-sucessido! Bem-vindo(a), %s.\n", login);
                pausar();
                return usuarios[i].tipo; // Retorna o tipo de usuario. 
            }    
        }

        tentativas++;
        printf("\nLogin ou senha incorretos. Tentativas restantes: %d.\n", MAX_TENTATIVAS - tentativas);
        pausar();
    
    }
    printf("\n Limite de tentavias excedido. O sistema sera encerrado.\n");
    pausar();
    return SAIR_SISTEMA;
}




