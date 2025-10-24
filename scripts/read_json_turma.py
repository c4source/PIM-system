import json
import sys
import os

if len(sys.argv) < 2:
    print("Erro: arquivo JSON não especificado")
    sys.exit(1)

arquivo_json = sys.argv[1]
professores_json = os.path.join(os.path.dirname(arquivo_json), "professores.json")

def carregar_dados(caminho):
    try:
        with open(caminho, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

turmas = carregar_dados(arquivo_json)
professores = carregar_dados(professores_json)
mapa_professores = {int(p["id"]): p["nome"] for p in professores}

print("========== LISTA DE TURMAS ==========\n")

if not turmas:
    print("Nenhuma turma cadastrada.")
    sys.exit(0)

for t in turmas:
    prof_nome = mapa_professores.get(int(t.get("professorId", -1)), "Sem professor")
    print(f"ID: {t.get('id')}")
    print(f"Nome da turma: {t.get('nome')}")
    print(f"Professor responsavel: {prof_nome}")
    print("-" * 40)
