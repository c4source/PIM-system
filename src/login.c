#include <stdio.h>
#include <string.h>
#include "login.h"   //inclui a definição da função realizarLogin().
#include "utils.h"  //inclui a definição da função LimparTela() e pausar().

//Contantes para os tipos de usuário e retorno.

#define ADMIN_ROLE 1       //Código de retorno para Administrador  
#define PROFESSOR_ROLE 2   //Código de retorno para Professor
#define ALUNO_ROLE 3       //Código de retorno para Aluno 
#define SAIR_SISTEMA -1    //Código de retorno para sair do sistema 
#define MAX_TENTATIVAS 3   // Número máximo de tentativas de Login

// Estrutura para armazenar credencias temporárias de Login.
typedef struct {

    char login[30];
    char senha[30];
    int tipo; //Tipo de usuarios: 1- Admin 2- Professor 3- Aluno

} Usuario;    //Usuario contem os atributos de login senha e tipo de usuario 

Usuario usuarios[] = { //Cria um novo tipo de dado 

    {"admin", "1234", ADMIN_ROLE},
    {"professor", "abcd", PROFESSOR_ROLE},
    {"aluno", "4321", ALUNO_ROLE},

};
int totalUsuarios = 3;

//Função para limpar o buffer 
void limparBufferEntrada() {
    int c;
    while ((c = getchar())) != '\n' && c != EOF;
}

int realizarLogin() {
    
    char login[30];
    char senha[30];
    int tentativas = 0; 

    while(tentativas < MAX_TENTATIVAS) {
        priontf("=====================================\n")
        printf("          TELA DE LOGIN (%d/%d)" + 1, MAX_TENTATIVAS);
        printf("=====================================\n\n")

        printf("Digite seu login: (ou 'sair' para encerrar): ");
        if (fgets(login, sizeof(loginm), stdin) == NULL) 
            return SAIR_SISTEMA;
       
        login[strcspn(login, "\n")] = '\0';  //Remove o caractere ENTER do final da string  
        
        if (strcmp(login, "sair") == 0) //Verifica se o usuario digitou 'sair' retornando o fim do programa.
            return SAIR_SISTEMA;

        printf("Digite sua senha: ");


    }

}




