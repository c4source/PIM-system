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

id_alvo = input("Digite o ID do professor que deseja editar: ").strip()

# procura professor pelo id
professor = None
for item in dados:
    if str(item.get("id")) == id_alvo:
        professor = item
        break

if professor is None:
    print("Professor nao encontrado.")
    sys.exit(1)

print(f"Editando professor ID {professor['id']} - {professor['nome']} (matricula: {professor['matricula']})")

novo_nome = input("Novo nome (Enter para manter): ").strip()
nova_matricula = input("Nova matricula (Enter para manter): ").strip()

if novo_nome:
    professor["nome"] = novo_nome
if nova_matricula:
    professor["matricula"] = nova_matricula

# salva alteracoes
with open(arquivo_json, "w") as f:
    json.dump(dados, f, indent=4)

print("Professor atualizado com sucesso!")
