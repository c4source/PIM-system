#include <stdio.h>
#include <stdlib.h>
#include "headers/administrador.h"
#include "headers/utils.h"

void listarAdministradores() {
    char output[2048];
    executarPython("scripts/read_json_administrador.py", "data/administradores.json", output, sizeof(output));
    printf("%s\n", output);
}

void cadastrarAdministrador() {
    systemPython("scripts/write_json_administrador.py", "data/administradores.json");
}

void editarAdministrador() {
    systemPython("scripts/edit_json_administrador.py", "data/administradores.json");
}

void excluirAdministrador() {
    systemPython("scripts/delete_json_administrador.py", "data/administradores.json");
}

