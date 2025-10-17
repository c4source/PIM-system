#include <stdio.h>
#include <stdlib.h>
#include "headers/aula.h"
#include "headers/utils.h"

void listarAulas() {
    char output[2048];
    executarPython("scripts/read_json_aulas.py", "data/aulas.json", output, sizeof(output));
    printf("%s\n", output);
}

void cadastrarAula() {
    systemPython("scripts/write_json_aulas.py", "data/aulas.json");
}

void editarAula() {
    systemPython("scripts/edit_json_aula.py", "data/aulas.json");
}

void excluirAula() {
    systemPython("scripts/delete_json_aula.py", "data/aulas.json");
}

