import json
import sys

if len(sys.argv) < 2:
    print("Erro: arquivo JSON nao especificado")
    sys.exit(1)

arquivo_json = sys.argv[1]

# Le os dados existentes, se o arquivo existir
try:
    with open(arquivo_json, "r") as f:
        dados = json.load(f)
except FileNotFoundError:
    dados = []
except json.JSONDecodeError:
    dados = []

# Gera automaticamente o proximo ID
if dados:
    novo_id = max(int(turma.get("id", 0)) for turma in dados) + 1
else:
    novo_id = 1

print("========== CADASTRO DE TURMA ==========\n")
# Solicita dados ao usuario
nova = {}
nova["id"] = novo_id
nova["nome"] = input("Digite o nome da turma: ")

dados.append(nova)

# Salva novamente no arquivo JSON
with open(arquivo_json, "w") as f:
    json.dump(dados, f, indent=4)

print("Cadastro realizado com sucesso!")
