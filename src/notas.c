#include <stdio.h>
#include <stdlib.h>
#include "headers/notas.h"
#include "headers/utils.h"
#include "headers/login.h"

void listarNotas() {
    char cmd[256];
    char output[4096];

    // Passa o arquivo + id_aluno
    sprintf(cmd, "data/notas.json %d", idUsuarioAtual);

    executarPython("scripts/read_json_nota.py", cmd, output, sizeof(output));

    printf("%s\n", output);
}




void cadastrarNota() {
    systemPython("scripts/write_json_nota.py", "data/notas.json");
}

void editarNota() {
    systemPython("scripts/edit_json_nota.py", "data/notas.json");
}