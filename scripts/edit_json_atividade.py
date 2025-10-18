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

print("========== EDIÇÃO DE ATIVIDADE ==========\n")

id_alvo = input("Digite o ID da atividade que deseja editar: ").strip()

# procura atividade pelo id
atividade = None
for item in dados:
    if str(item.get("id")) == id_alvo:
        atividade = item
        break

if atividade is None:
    print("Atividade nao encontrada.")
    sys.exit(1)

print(f"Editando Atividade ID {atividade['id']} - {atividade['titulo']}")

novo_titulo = input("Novo titulo (Enter para manter): ").strip()
nova_descricao = input("Nova Descricao (Enter para manter): ").strip()
nova_nota = input("Nova nota (Enter p/ manter): ").strip()

if novo_titulo:
    atividade["titulo"] = novo_titulo
if nova_descricao:
    atividade["descricao"] = nova_descricao
if nova_nota:
    atividade["nota"] = float(nova_nota)


# salva alteracoes
with open(arquivo_json, "w") as f:
    json.dump(dados, f, indent=4)

print("Registro atualizado com sucesso!")
