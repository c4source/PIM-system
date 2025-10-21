import json
import sys
import os

NOTAS_JSON = "data/notas.json"
ALUNOS_JSON = "data/alunos.json"
ATIVIDADES_JSON = "data/atividades.json"

def carregar_dados(caminho):
    try:
        with open(caminho, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

notas = carregar_dados(NOTAS_JSON)
alunos = carregar_dados(ALUNOS_JSON)
atividades = carregar_dados(ATIVIDADES_JSON)

print("========== RELATÓRIO DE NOTAS ==========\n")

if not notas:
    print("Nenhuma nota cadastrada.")
    sys.exit(0)

print("1. Ver notas por aluno")
print("2. Ver notas por atividade")
op = input("\nEscolha uma opção: ").strip()

if op == "1":
    for a in alunos:
        print(f"{a['id']}. {a['nome']}")
    try:
        aluno_id = int(input("\nDigite o ID do aluno: ").strip())
    except ValueError:
        sys.exit(1)
    aluno = next((a for a in alunos if int(a["id"]) == aluno_id), None)
    if not aluno:
        print("Aluno não encontrado.")
        sys.exit(1)
    notas_aluno = [n for n in notas if int(n["alunoId"]) == aluno_id]
    print(f"\nNotas do aluno {aluno['nome']}:\n")
    if not notas_aluno:
        print("Nenhuma nota registrada.")
    else:
        for n in notas_aluno:
            atividade_nome = next((a["titulo"] for a in atividades if int(a["id"]) == int(n["atividadeId"])), "Desconhecida")
            print(f"- {atividade_nome}: {n['nota']} ({n['status']})")

elif op == "2":
    for a in atividades:
        print(f"{a['id']}. {a['titulo']}")
    try:
        atv_id = int(input("\nDigite o ID da atividade: ").strip())
    except ValueError:
        sys.exit(1)
    atividade = next((a for a in atividades if int(a["id"]) == atv_id), None)
    if not atividade:
        print("Atividade não encontrada.")
        sys.exit(1)
    notas_atividade = [n for n in notas if int(n["atividadeId"]) == atv_id]
    print(f"\nNotas da atividade {atividade['titulo']}:\n")
    if not notas_atividade:
        print("Nenhum aluno respondeu.")
    else:
        soma = 0
        for n in notas_atividade:
            aluno_nome = next((a["nome"] for a in alunos if int(a["id"]) == int(n["alunoId"])), "Desconhecido")
            soma += n["nota"]
            print(f"- {aluno_nome}: {n['nota']} ({n['status']})")
        if notas_atividade:
            media = soma / len(notas_atividade)
            print(f"\nMédia da turma: {media:.2f}")
