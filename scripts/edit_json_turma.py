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

id_alvo = input("Digite o ID da turma que deseja editar: ").strip()

# procura turma pelo id
turma = None
for item in dados:
    if str(item.get("id")) == id_alvo:
        turma = item
        break

if administrador is None:
    print("Turma nao encontrada.")
    sys.exit(1)

print(f"Editando Turma ID {turma['id']} - {turma['nome']} ")

novo_nome = input("Novo nome (Enter para manter): ").strip()

if novo_nome:
    administrador["nome"] = novo_nome

# salva alteracoes
with open(arquivo_json, "w") as f:
    json.dump(dados, f, indent=4)

print("Turma atualizada com sucesso!")
