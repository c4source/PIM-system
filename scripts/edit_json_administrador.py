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

id_alvo = input("Digite o ID do administrador que deseja editar: ").strip()

# procura administrador pelo id
administrador = None
for item in dados:
    if str(item.get("id")) == id_alvo:
        administrador = item
        break

if administrador is None:
    print("Administrador nao encontrado.")
    sys.exit(1)

print(f"Editando Administrador ID {administrador['id']} - {administrador['nome']} ")

novo_nome = input("Novo nome (Enter para manter): ").strip()
novo_email = input("Novo e-mail (Enter para manter): ").strip()
nova_senha = input("Novo senha (Enter para manter): ").strip()

if novo_nome:
    administrador["nome"] = novo_nome
if novo_email:
    administrador["email"] = novo_email
if nova_senha:
    administrador["senha"] = nova_senha

# salva alteracoes
with open(arquivo_json, "w") as f:
    json.dump(dados, f, indent=4)

print("Administrador atualizado com sucesso!")
