#include <stdio.h>
#include <stdlib.h>
#include "headers/aula.h"
#include "headers/utils.h"
#include "headers/login.h"

void listarAulas() {
    char cmd[256];
    char output[4096];

    // Passa o arquivo + o ID do professor
    sprintf(cmd, "data/aulas.json %d", idUsuarioAtual);

    executarPython("scripts/read_json_aula.py", cmd, output, sizeof(output));

    printf("%s\n", output);
}




void cadastrarAula() {
    systemPython("scripts/write_json_aula.py", "data/aulas.json");
}

void editarAula() {
    systemPython("scripts/edit_json_aula.py", "data/aulas.json");
}

void excluirAula() {
    systemPython("scripts/delete_json_aula.py", "data/aulas.json");
}

