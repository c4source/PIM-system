#ifndef UTILS_H
#define UTILS_H

// Declaração das funções
void executarPython(const char *script, const char *param, char *output, int size);
void systemPython(const char *script, const char *param);
void construirCaminho(char *destino, const char *subcaminho);

#endif
