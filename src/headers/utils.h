#ifndef UTILS_H
#define UTILS_H

// --- UI helpers usados por login.c e menus ---
void limparTela(void);
void pausar(void);

// Declaração das funções
void executarPython(const char *script, const char *param, char *output, int size);
void systemPython(const char *script, const char *param);
void construirCaminho(char *destino, const char *subcaminho);

#endif
