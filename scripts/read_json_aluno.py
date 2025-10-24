import json
import sys
import os

if len(sys.argv) < 2:
    print("Erro: arquivo JSON não especificado")
    sys.exit(1)

arquivo_json = sys.argv[1]
turmas_json = os.path.join(os.path.dirname(arquivo_json), "turmas.json")

def carregar_dados(caminho):
    try:
        with open(caminho, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

try:
    print("========== LISTA DE ALUNOS MATRICULADOS ==========\n")

    alunos = carregar_dados(arquivo_json)
    turmas = carregar_dados(turmas_json)

    if not alunos:
        print("Nenhum aluno cadastrado.")
        sys.exit(0)

    # Cria um dicionário para buscar nome da turma rapidamente
    mapa_turmas = {int(t.get("id", -1)): t.get("nome", "Turma desconhecida") for t in turmas}

    for item in alunos:
        turma_id = item.get("turmaId")
        nome_turma = mapa_turmas.get(int(turma_id), "Não associada")

        print(f"ID: {item.get('id')}")
        print(f"Nome: {item.get('nome')}")
        print(f"E-mail: {item.get('email')}")
        print(f"Turma: {nome_turma}")
        print("-" * 40)

except FileNotFoundError:
    print("Arquivo não encontrado:", arquivo_json)
except json.JSONDecodeError:
    print("Erro ao ler JSON:", arquivo_json)
