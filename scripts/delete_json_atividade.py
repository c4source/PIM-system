import json
import sys

if len(sys.argv) < 2:
    print("Erro: arquivo JSON não especificado")
    sys.exit(1)

arquivo_json = sys.argv[1]

try:
    with open(arquivo_json, "r", encoding="utf-8") as f:
        dados = json.load(f)
except (FileNotFoundError, json.JSONDecodeError):
    print("Erro: arquivo não encontrado ou vazio.")
    sys.exit(1)

print("========== EXCLUSAO DE ATIVIDADE ==========\n")
id_alvo = input("Digite o ID da atividade que deseja excluir: ").strip()

try:
    id_alvo = int(id_alvo)
except ValueError:
    print("Erro: o ID deve ser um número inteiro.")
    sys.exit(1)

indice = next((i for i, a in enumerate(dados) if int(a.get("id", -1)) == id_alvo), None)

if indice is None:
    print("Atividade não encontrada.")
    sys.exit(1)

atividade = dados[indice]
confirm = input(f"Confirmar exclusão da atividade '{atividade['titulo']}' (ID {atividade['id']})? (s/n): ").strip().lower()
if confirm != "s":
    print("Exclusão cancelada.")
    sys.exit(0)

dados.pop(indice)

with open(arquivo_json, "w", encoding="utf-8") as f:
    json.dump(dados, f, indent=4, ensure_ascii=False)

print("Registro excluido com sucesso!")
