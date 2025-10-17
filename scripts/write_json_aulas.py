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

# Solicita dados ao usuario
nova = {}
nova["id"] = input("Digite o ID da aula: ")
nova["professorId"] = input("Digite o id do professor: ")
nova["tema"] = input("Digite o tema da aula: ")

dados.append(nova)

# Salva novamente no arquivo JSON
with open(arquivo_json, "w") as f:
    json.dump(dados, f, indent=4)

print("Aula cadastrada com sucesso!")
