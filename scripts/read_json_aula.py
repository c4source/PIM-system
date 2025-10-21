import json
import sys
import os

if len(sys.argv) < 2:
    print("Erro: arquivo JSON não especificado")
    sys.exit(1)

arquivo_json = sys.argv[1]
turmas_json = os.path.join(os.path.dirname(arquivo_json), "turmas.json")
professores_json = os.path.join(os.path.dirname(arquivo_json), "professores.json")

def carregar_dados(caminho):
    try:
        with open(caminho, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

# --- Carrega dados ---
aulas = carregar_dados(arquivo_json)
turmas = carregar_dados(turmas_json)
professores = carregar_dados(professores_json)

print("========== LISTA DE AULAS ==========\n")

if not aulas:
    print("Nenhuma aula cadastrada.")
    sys.exit(0)

# --- Cria dicionários para consultas rápidas ---
mapa_turmas = {int(t["id"]): t["nome"] for t in turmas}
mapa_professores = {int(p["id"]): p["nome"] for p in professores}

# --- Exibe as aulas ---
for a in aulas:
    turma_nome = mapa_turmas.get(int(a.get("turmaId", -1)), "Turma não encontrada")
    prof_nome = mapa_professores.get(int(a.get("professorId", -1)), "Professor não encontrado")
    print(f"ID: {a.get('id')}")
    print(f"Tema: {a.get('tema')}")
    print(f"Turma: {turma_nome}")
    print(f"Professor responsável: {prof_nome}")
    print("-" * 40)
