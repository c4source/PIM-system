#include <stdio.h>
#include <stdlib.h>
#include "headers/utils.h" //Inclui a definição da função LimparTela() e pausar().

void limparTela(void) {
#ifdef _WIN32
    system("cls");
#else
    system("clear");
#endif
}

void pausar(void) {
    printf("Pressione ENTER para continuar...");
    getchar();

}

void limparBufferEntrada(void) {
    int c;
    while ((c = getchar()) != '\n' && c != EOF);

}