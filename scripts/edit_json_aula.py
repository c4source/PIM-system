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

id_alvo = input("Digite o ID da aula que deseja editar: ").strip()

# procura aula pelo id
aula = None
for item in dados:
    if str(item.get("id")) == id_alvo:
        atividade = item
        break

if aula is None:
    print("aula nao encontrada.")
    sys.exit(1)

print(f"Editando Aula ID {aula['id']}")

novo_tema = input("Novo tema (Enter para manter): ").strip()


if novo_tema:
    aula["tema"] = novo_tema

# salva alteracoes
with open(arquivo_json, "w") as f:
    json.dump(dados, f, indent=4)

print("Aula atualizada com sucesso!")
