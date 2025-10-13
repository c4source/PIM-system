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

# Solicita dados ao usuario
nova = {}
nova["id"] = input("Digite o ID da turma: ")
nova["nome"] = input("Digite o nome da turma: ")
nova["periodo"] = input("Digite o periodo da turma: ")

dados.append(nova)

# Salva novamente no arquivo JSON
with open(arquivo_json, "w") as f:
    json.dump(dados, f, indent=4)

print("Turma cadastrada com sucesso!")
