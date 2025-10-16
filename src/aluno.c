#include <stdio.h>
#include <stdlib.h>
#include "headers/aluno.h"
#include "headers/utils.h"

void listarAlunos() {
    char output[2048];
    executarPython("scripts/read_json_aluno.py", "data/alunos.json", output, sizeof(output));
    printf("%s\n", output);
}

void cadastrarAluno() {
    systemPython("scripts/write_json_aluno.py", "data/alunos.json");
}

void editarAluno() {
    systemPython("scripts/edit_json_aluno.py", "data/alunos.json");
}

void excluirAluno() {
    systemPython("scripts/delete_json_aluno.py", "data/alunos.json");
}

