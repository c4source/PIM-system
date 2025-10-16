import json
import sys

if len(sys.argv) < 2:
    print("Erro: arquivo JSON nao especificado")
    sys.exit(1)

arquivo_json = sys.argv[1]

try:
    with open(arquivo_json, "r") as f:
        dados = json.load(f)
except (FileNotFoundError, json.JSONDecodeError):
    print("Erro: arquivo nao encontrado ou vazio.")
    sys.exit(1)

id_alvo = input("Digite o ID do administrador que deseja excluir: ").strip()

# encontra indice do administrador
indice = next((i for i, a in enumerate(dados) if str(a.get("id")) == id_alvo), None)

if indice is None:
    print("Administrador nao encontrado.")
    sys.exit(1)

aluno = dados[indice]
confirm = input(f"Confirmar exclusao do administrador {administrador['nome']} (ID {administrador['id']})? (s/n): ").strip().lower()
if confirm != "s":
    print("Exclusao cancelada.")
    sys.exit(0)

dados.pop(indice)

with open(arquivo_json, "w") as f:
    json.dump(dados, f, indent=4)

print("Administrador excluido com sucesso!")
