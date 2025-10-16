#include <stdio.h>
#include <stdlib.h>
#include <conio.h>
#include "headers/aluno.h"
#include "headers/turma.h"
#include "headers/aula.h"
#include "headers/atividade.h"
#include "headers/professor.h"

void menuPrincipal();
void menuAlunos();
void menuTurmas();
void menuAulas();
void menuAtividades();
void menuProfessores();

int main() {
    menuPrincipal();
    return 0;
}

void menuPrincipal(){
    int opcao;

    do{
        system("cls");

        printf("==========MENU PRINCIPAL==========\n");
        printf("1. Menu de Alunos\n");
        printf("2. Menu de Professores\n");
        printf("3. Menu de Atividades\n");
        printf("4. Menu de Aulas\n");
        printf("5. Menu de Turmas\n");
        printf("6. Menu do Administrador\n");
        printf("7. Encerrar o Programa\n");
        printf("\nEscolha uma opcao: ");

        scanf("%d", &opcao);

        switch (opcao)
        {
        case 1:
            menuAlunos();
            break;
        case 2:
            menuProfessores();
            break;
        
        default:
            break;
        }


    }while(opcao != 7);
}

void menuAlunos(){
    int opcao;
    do{
        system("cls");

        printf("==========MENU DE ALUNOS==========\n");
        printf("1. Cadastrar Aluno\n");
        printf("2. Editar Aluno\n");
        printf("3. Excluir Aluno\n");
        printf("4. Lista de Alunos\n");
        printf("5. Voltar ao Menu Anterior\n");
        printf("\nEscolha uma opcao: ");

        scanf("%d", &opcao);

        switch (opcao)
        {
        case 1:
            system("cls");
            cadastrarAluno();
            _getch();
            break;
        case 2:
            system("cls");
            editarAluno();
            _getch();
            break;
        case 3:
            system("cls");
            excluirAluno();
            _getch();
            break;
        case 4:
            system("cls");
            listarAlunos();
            printf("Pressione qualquer tecla para Fechar a listagem de alunos.");
            _getch();
            break;
        case 5:
            printf("Voltando ao menu Principal...");
            break;
        default:
            break;
        }

    }while(opcao != 5 );
}

void menuProfessores(){
    int opcao;

    do{
        system("cls");

        printf("==========MENU DE PROFESSORES==========\n");
        printf("1. Cadastrar Professor\n");
        printf("2. Editar Professor\n");
        printf("3. Excluir Professor\n");
        printf("4. Lista de Professores\n");
        printf("5. Voltar ao Menu Anterior\n");
        printf("\nEscolha uma opcao: ");

        scanf("%d", &opcao);

        switch (opcao)
        {
        case 1:
            system("cls");
            cadastrarProfessor();
            _getch();
            break;
        case 2:
            system("cls");
            editarProfessor();
            _getch();
            break;
        case 3:
            system("cls");
            excluirProfessor();
            _getch();
            break;
        case 4:
            system("cls");
            listarProfessores();
            printf("Pressione qualquer tecla para Fechar a listagem de professores.");
            _getch();
            break;
        case 5:
            printf("Voltando ao menu Principal...");
            break;
        default:
            break;
        }

        }while(opcao != 5 );

}