#include <stdio.h>
#include <stdlib.h>
#include "headers/notas.h"
#include "headers/utils.h"

void listarNotas() {
    systemPython("scripts/read_json_nota.py", "data/notas.json");
}

void cadastrarNota() {
    systemPython("scripts/write_json_nota.py", "data/notas.json");
}

void editarNota() {
    systemPython("scripts/edit_json_nota.py", "data/notas.json");
}