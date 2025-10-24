#include <stdio.h>
#include <stdlib.h>
#include "headers/atividade.h"
#include "headers/utils.h"
#include "headers/login.h"

void listarAtividades() {
    char cmd[256];
    char output[4096];

    // Passa o arquivo + id_usuario + tipo_usuario
    sprintf(cmd, "data/atividades.json %d %d", idUsuarioAtual, tipoUsuarioAtual);

    executarPython("scripts/read_json_atividade.py", cmd, output, sizeof(output));

    printf("%s\n", output);
}



void cadastrarAtividade() {
    systemPython("scripts/write_json_atividade.py", "data/atividades.json");
}

void editarAtividade() {
    systemPython("scripts/edit_json_atividade.py", "data/atividades.json");
}

void excluirAtividade() {
    systemPython("scripts/delete_json_atividade.py", "data/atividades.json");
}
