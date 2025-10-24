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

def salvar_dados(caminho, dados):
    with open(caminho, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)

def proximo_id(lista):
    return (max(int(x.get("id", 0)) for x in lista) + 1) if lista else 1

# Carrega dados existentes
turmas = carregar_dados(arquivo_json)
professores = carregar_dados(professores_json)

print("========== CADASTRO DE TURMA ==========\n")

nova = {}
nova["id"] = proximo_id(turmas)
nova["nome"] = input("Digite o nome da turma: ").strip()

# Seleção de professor responsável
if not professores:
    print("\n⚠️ Nenhum professor cadastrado. Cadastre um professor antes de associar.")
    nova["professorId"] = None
else:
    print("\nProfessores disponíveis:")
    for p in professores:
        print(f"{p['id']}. {p['nome']}")
    try:
        prof_id = int(input("Digite o ID do professor responsável: ").strip())
        if any(int(p.get("id", -1)) == prof_id for p in professores):
            nova["professorId"] = prof_id
        else:
            print("Professor não encontrado. A turma será cadastrada sem professor.")
            nova["professorId"] = None
    except ValueError:
        print("Entrada inválida. A turma será cadastrada sem professor.")
        nova["professorId"] = None

turmas.append(nova)
salvar_dados(arquivo_json, turmas)

print(f"\nTurma cadastrada com sucesso! ID: {nova['id']}")
if nova["professorId"]:
    prof_nome = next((p["nome"] for p in professores if int(p["id"]) == nova["professorId"]), None)
    print(f"Professor responsável: {prof_nome}")
else:
    print("Turma cadastrada sem professor associado.")
