import json
import sys

TURMAS_JSON = "data/turmas.json"
ALUNOS_JSON = "data/alunos.json"

def carregar_json(caminho):
    try:
        with open(caminho, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        print(f"Erro ao ler {caminho}")
        return []

def gerar_relatorio_turma(turma_id):
    turmas = carregar_json(TURMAS_JSON)
    alunos = carregar_json(ALUNOS_JSON)

    turma = next((t for t in turmas if int(t.get("id", -1)) == turma_id), None)
    if not turma:
        print(f"Turma com ID {turma_id} não encontrada.")
        return

    alunos_turma = [a for a in alunos if int(a.get("turmaId", -1)) == turma_id]

    print(f"========== RELATÓRIO DE TURMA ==========")
    print(f"Turma: {turma['nome']} (ID: {turma['id']})\n")
    if not alunos_turma:
        print("Nenhum aluno matriculado nesta turma.")
        return

    print("Alunos matriculados:")
    for aluno in alunos_turma:
        print(f"- {aluno['nome']} (ID: {aluno['id']})")

    print(f"\nTotal de alunos: {len(alunos_turma)}")

if __name__ == "__main__":
    try:
        turma_id = int(input("Digite o ID da turma: ").strip())
    except ValueError:
        print("Erro: ID inválido.")
        sys.exit(1)

    gerar_relatorio_turma(turma_id)
