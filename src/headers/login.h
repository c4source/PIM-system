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

extern int tipoUsuarioAtual;
extern int idUsuarioAtual;
extern char usuarioNome[128];
void lerSenhaOculta(char *dest, int maxlen, int mostrarAsterisco);

int validarCredenciais(const char *email, const char *senha);

int realizarLogin(void);

#endif // LOGIN_H