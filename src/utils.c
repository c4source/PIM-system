#include "headers/utils.h"
#include <windows.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Constrói caminho absoluto real para o arquivo, baseado na raiz do projeto
void construirCaminho(char *destino, const char *subcaminho) {
    char caminhoExe[MAX_PATH];
    GetModuleFileName(NULL, caminhoExe, MAX_PATH);

    // Remove o nome do exe
    char *p = strrchr(caminhoExe, '\\');
    if (p) *p = '\0';

    // Caminho raiz = pai da pasta build se exe estiver em build
    char raiz[MAX_PATH];
    strncpy(raiz, caminhoExe, MAX_PATH);
    if (strstr(raiz, "\\build") != NULL)
        *strstr(raiz, "\\build") = '\0';

    // Corrige barras no subcaminho
    char sub[MAX_PATH];
    strncpy(sub, subcaminho, MAX_PATH);
    for (int i = 0; sub[i]; i++)
        if (sub[i] == '/') sub[i] = '\\';

    // Combina raiz + subcaminho
    char combinado[MAX_PATH];
    snprintf(combinado, sizeof(combinado), "%s\\%s", raiz, sub);

    // Converte para caminho absoluto real
    char absoluto[MAX_PATH];
    GetFullPathName(combinado, MAX_PATH, absoluto, NULL);
    strncpy(destino, absoluto, MAX_PATH);
}

// Executa script Python e captura saída
void executarPython(const char *script, const char *param, char *output, int size) {
    char caminhoScript[MAX_PATH];
    char caminhoParam[MAX_PATH];
    char comando[512];

    construirCaminho(caminhoScript, script);
    construirCaminho(caminhoParam, param);
    snprintf(comando, sizeof(comando), "python \"%s\" \"%s\"", caminhoScript, caminhoParam);

    FILE *pipe = _popen(comando, "r");
    if (!pipe) {
        snprintf(output, size, "Erro ao executar script Python.");
        return;
    }

    char linha[256];
    output[0] = '\0';
    while (fgets(linha, sizeof(linha), pipe) != NULL) {
        if ((strlen(output) + strlen(linha)) < (size_t)size)
            strcat(output, linha);
    }

    _pclose(pipe);
}

// Executa script Python sem capturar saída (para cadastro)
void systemPython(const char *script, const char *param) {
    char caminhoScript[MAX_PATH];
    char caminhoParam[MAX_PATH];
    char comando[512];

    construirCaminho(caminhoScript, script);
    construirCaminho(caminhoParam, param);
    snprintf(comando, sizeof(comando), "python \"%s\" \"%s\"", caminhoScript, caminhoParam);

    system(comando);
}
