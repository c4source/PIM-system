#include <stdio.h>
#include <stdlib.h>
#include "headers/turma.h"
#include "headers/utils.h"

void listarTurmas() {
    char output[2048];
    executarPython("scripts/read_json_turma.py", "data/turmas.json", output, sizeof(output));
    printf("%s\n", output);
}

void cadastrarTurma() {
    systemPython("scripts/write_json_turma.py", "data/turmas.json");
}

void editarTurma() {
    systemPython("scripts/edit_json_turma.py", "data/turmas.json");
}

void excluirTurma() {
    systemPython("scripts/delete_json_turma.py", "data/turmas.json");
}

