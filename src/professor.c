#include <stdio.h>
#include <stdlib.h>
#include "headers/professor.h"
#include "headers/utils.h"

void listarProfessores() {
    char output[2048];
    executarPython("scripts/read_json_professor.py", "data/professores.json", output, sizeof(output));
    printf("%s\n", output);
}

void cadastrarProfessor() {
    systemPython("scripts/write_json_professor.py", "data/professores.json");
}