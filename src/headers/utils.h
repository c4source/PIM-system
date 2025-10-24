#ifndef UTILS_H
#define UTILS_H

// --- UI helpers usados por login.c e menus ---
void limparTela(void);
void pausar(void);

// Declaração das funções
void executarPython(const char *script, const char *param, char *output, int size);

// Executa um script Python diretamente no terminal (sem capturar saída)
void systemPython(const char *script, const char *param);

// Constrói um caminho seguro baseado na raiz do projeto
void construirCaminho(char *destino, const char *subcaminho);

// Limpa o terminal (Windows ou Linux)
void limparTela(void);

// Pausa até o usuário pressionar Enter
void pausar(void);

#endif // UTILS_H
