import json
import sys

if len(sys.argv) < 2:
    print("Erro: arquivo JSON não especificado")
    sys.exit(1)

arquivo_json = sys.argv[1]

try:
    print("========== LISTA DE AULAS ==========\n")
    with open(arquivo_json, "r", encoding="utf-8") as f:
        dados = json.load(f)
        if not dados:
            print("Nenhuma aula cadastrada.")
        for item in dados:
            print(f"ID: {item.get('id')}")
            print(f"Professor ID: {item.get('professorId')}")
            print(f"Turma ID: {item.get('turmaId')}")
            print(f"Tema: {item.get('tema')}")
            print("-" * 40)
except FileNotFoundError:
    print("Arquivo não encontrado:", arquivo_json)
except json.JSONDecodeError:
    print("Erro ao ler JSON:", arquivo_json)
