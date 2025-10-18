import json
import sys

if len(sys.argv) < 2:
    print("Erro: arquivo JSON nao especificado")
    sys.exit(1)

arquivo_json = sys.argv[1]

# Le os dados existentes
try:
    with open(arquivo_json, "r") as f:
        dados = json.load(f)
except FileNotFoundError:
    dados = []
except json.JSONDecodeError:
    dados = []

# Gera automaticamente o proximo ID
if dados:
    novo_id = max(int(aula.get("id", 0)) for aula in dados) + 1
else:
    novo_id = 1

print("========== CADASTRO DE AULA ==========\n")
# Solicita dados ao usuario
nova = {}
nova["id"] = novo_id
nova["professorId"] = int(input("ID do professor: ").strip())
nova["tema"] = input("Digite o tema da aula: ")

dados.append(nova)

# Salva novamente no arquivo JSON
with open(arquivo_json, "w") as f:
    json.dump(dados, f, indent=4)

print("Cadastro realizado com sucesso!")
