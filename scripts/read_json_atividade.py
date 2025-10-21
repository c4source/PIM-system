import json
import sys
import os

if len(sys.argv) < 2:
    print("Erro: arquivo JSON não especificado")
    sys.exit(1)

arquivo_json = sys.argv[1]
turmas_json = os.path.join(os.path.dirname(arquivo_json), "turmas.json")
aulas_json = os.path.join(os.path.dirname(arquivo_json), "aulas.json")
professores_json = os.path.join(os.path.dirname(arquivo_json), "professores.json")

def carregar_dados(caminho):
    try:
        with open(caminho, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

# --- Carrega dados ---
atividades = carregar_dados(arquivo_json)
turmas = carregar_dados(turmas_json)
aulas = carregar_dados(aulas_json)
professores = carregar_dados(professores_json)

print("========== LISTA DE ATIVIDADES ==========\n")

if not atividades:
    print("Nenhuma atividade cadastrada.")
    sys.exit(0)

# --- Cria dicionários de busca rápida ---
mapa_turmas = {int(t["id"]): t["nome"] for t in turmas}
mapa_aulas = {int(a["id"]): a["tema"] for a in aulas}
mapa_professores = {int(p["id"]): p["nome"] for p in professores}

# --- Exibe todas as atividades ---
for a in atividades:
    turma_nome = mapa_turmas.get(int(a.get("turmaId", -1)), "Turma não encontrada")
    aula_nome = mapa_aulas.get(int(a.get("aulaId", -1)), "Aula não encontrada")
    prof_nome = mapa_professores.get(int(a.get("professorId", -1)), "Professor não encontrado")

    print(f"ID: {a.get('id')}")
    print(f"Título: {a.get('titulo')}")
    print(f"Descrição: {a.get('descricao')}")
    print(f"Turma: {turma_nome}")
    print(f"Aula: {aula_nome}")
    print(f"Professor responsável: {prof_nome}")
    print("-" * 40)
