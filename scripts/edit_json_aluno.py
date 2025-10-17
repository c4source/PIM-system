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

id_alvo = input("Digite o ID do aluno que deseja editar: ").strip()

# procura aluno pelo id
aluno = None
for item in dados:
    if str(item.get("id")) == id_alvo:
        aluno = item
        break

if aluno is None:
    print("Aluno nao encontrado.")
    sys.exit(1)

print(f"Editando aluno ID {aluno['id']} - {aluno['nome']} (matricula: {aluno['matricula']})")

novo_nome = input("Novo nome (Enter para manter): ").strip()
nova_matricula = input("Nova matricula (Enter para manter): ").strip()

if novo_nome:
    aluno["nome"] = novo_nome
if nova_matricula:
    aluno["matricula"] = nova_matricula

# salva alteracoes
with open(arquivo_json, "w") as f:
    json.dump(dados, f, indent=4)

print("Aluno atualizado com sucesso!")
