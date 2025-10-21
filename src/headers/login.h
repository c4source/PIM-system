#ifndef LOGIN_H
#define LOGIN_H

// Códigos de retorno (papéis)
#define ADMIN_ROLE       1
#define PROFESSOR_ROLE   2
#define ALUNO_ROLE       3

// Controle de fluxo
#define SAIR_SISTEMA    -1
#define MAX_TENTATIVAS   3

// Exibe a tela de login, chama o validador Python e retorna:
//  1=admin, 2=professor, 3=aluno, -1=sair
int realizarLogin(void);

#endif // LOGIN_H