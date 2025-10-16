#ifndef LOGIN_H
#define LOGIN_H 

// ==================================================
// Arquivo: login.h 
// Descrição: Declarações e definições do modulo login
// ===================================================

// ---- Constantes para os tipos de usuario e retorno ---- 

#define ADMIN_ROLE 1    //Código de retorno para Administrador 
#define PROFESSOR_ROLE 2 //Código de retorno para Professor 
#define ALUNO_ROLE 3  //Código de retorno para aluno 
#define SAIR_SISTEMA -1 //Código de retorno para sair do sistema
#define MAX_TENTATIVAS 3 // Número máximo de tentativas de login
#define TENTATIVA_FALHA 0 //Código de retorno para tentativas falhas 


// ---- Estrutua para armazenar credenciais temporárias de login ---- 

typedef struct {
    char login[30];
    char senha[30];
    int tipo; 
} Usuario;

//Protótipos de funções 

int realizarLogin(void);
void limparBufferEntrada(void);

#endif 