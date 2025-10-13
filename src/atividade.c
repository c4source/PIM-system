#include <stdio.h>
#include <stdlib.h>
#include "headers/atividade.h"
#include "headers/utils.h"

void listarAtividades() {
    char output[2048];
    executarPython("scripts/read_json_atividades.py", "data/atividades.json", output, sizeof(output));
    printf("%s\n", output);
}

void cadastrarAtividade() {
    systemPython("scripts/write_json_atividades.py", "data/atividades.json");
    printf("Atividade cadastrada com sucesso!\n");
}
