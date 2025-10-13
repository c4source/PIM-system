#include <stdio.h>
#include "headers/aluno.h"
#include "headers/turma.h"
#include "headers/aula.h"
#include "headers/atividade.h"

int main() {
    int opcao;

    do {
        printf("\n==== Sistema Academico ====\n");
        printf("1. Listar alunos\n");
        printf("2. Cadastrar aluno\n");
        printf("3. Listar turmas\n");
        printf("4. Cadastrar turma\n");
        printf("5. Listar aulas\n");
        printf("6. Cadastrar aula\n");
        printf("7. Listar atividades\n");
        printf("8. Cadastrar atividade\n");
        printf("9. Sair\n");
        printf("Escolha uma opcao: ");

        if (scanf("%d", &opcao) != 1) {
            while (getchar() != '\n'); // limpa buffer
            opcao = 0;
        }

        switch(opcao) {
            case 1: listarAlunos(); break;
            case 2: cadastrarAluno(); break;
            case 3: listarTurmas(); break;
            case 4: cadastrarTurma(); break;
            case 5: listarAulas(); break;
            case 6: cadastrarAula(); break;
            case 7: listarAtividades(); break;
            case 8: cadastrarAtividade(); break;
            case 9: printf("Saindo do sistema...\n"); break;
            default: printf("Opcao invalida! Tente novamente.\n");
        }

    } while(opcao != 9);

    return 0;
}
