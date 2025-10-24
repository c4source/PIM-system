import json
import os
import sys

PROFESSORES_JSON = "data/professores.json"
TURMAS_JSON = "data/turmas.json"

def carregar_json(caminho):
    try:
        with open(caminho, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        print(f"Erro ao ler {caminho}")
        return []

def gerar_relatorio_professor(professor_id):
    professores = carregar_json(PROFESSORES_JSON)
    turmas = carregar_json(TURMAS_JSON)

    professor = next((p for p in professores if int(p.get("id", -1)) == professor_id), None)
    if not professor:
        print(f"Professor com ID {professor_id} nao encontrado.")
        return

    turmas_professor = [t for t in turmas if int(t.get("professorId", -1)) == professor_id]

    print("========== RELATORIO DE PROFESSOR ==========")
    print(f"Professor: {professor['nome']} (ID: {professor['id']})")
    print(f"E-mail: {professor.get('email', 'sem e-mail')}\n")

    if not turmas_professor:
        print("⚠️ Nenhuma turma associada a este professor.")
        return

    print("Turmas sob responsabilidade:")
    for turma in turmas_professor:
        print(f"- {turma['nome']} (ID: {turma['id']})")

    print(f"\nTotal de turmas: {len(turmas_professor)}")

if __name__ == "__main__":
    try:
        professor_id = int(input("Digite o ID do professor: ").strip())
    except ValueError:
        print("Erro: ID inválido.")
        sys.exit(1)

    gerar_relatorio_professor(professor_id)
